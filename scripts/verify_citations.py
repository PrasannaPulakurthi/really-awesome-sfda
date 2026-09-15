#!/usr/bin/env python3
"""Verify citations in README.md against primary bibliographic sources.

This list is deliberately comprehensive rather than curated, so the checks here
test whether a citation is **accurate**, not whether the venue is prestigious.
A WACV paper and a CVPR paper are held to exactly the same standard: the
identifier must resolve to the paper the entry names, and the venue tag must
match what the record says.

What this catches:
  * An identifier that resolves to a different paper than the entry names.
    This is the most common way a wrong citation enters a list.
  * A venue tag that disagrees with the Crossref record for that paper,
    including a main-conference tag on a workshop paper.
  * A code repository that no longer exists.
  * An entry nothing could identify, which is reported rather than passed over.
  * A publication year that disagrees with the record by more than one
    (early access routinely shifts a year, so only larger gaps are reported).

What this cannot catch:
  * Whether the entry's title faithfully describes the paper's contribution.
    That remains a human reading the paper.

Entry format understood by this script:

    - Title of the paper [`paper`](url) [`code`](url) `Venue'YY`

Exit codes:
  0  no hard failures
  1  at least one hard failure

Usage:
  python scripts/verify_citations.py                     # everything
  python scripts/verify_citations.py --only SFDA         # matching entries
  python scripts/verify_citations.py --diff-base main    # only what changed
  python scripts/verify_citations.py --markdown          # PR comment report
"""

import argparse
import html
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field

# Venues seen in this list. Accepting a venue here means "this abbreviation is
# known and can be checked", not "this venue is elite" - the list is
# comprehensive by design.
VENUE_PATTERNS = {
    "CVPR": (["conference on computer vision and pattern recognition"], ["workshop"]),
    "CVPRW": (["computer vision and pattern recognition workshops"], []),
    "ICCV": (["international conference on computer vision"], ["workshop"]),
    "ECCV": (["european conference on computer vision", "lecture notes in computer science"], []),
    "WACV": (["winter conference on applications of computer vision"], []),
    "BMVC": (["british machine vision"], []),
    "TPAMI": (["transactions on pattern analysis"], []),
    "IJCV": (["international journal of computer vision"], []),
    "TIP": (["transactions on image processing"], []),
    "TMM": (["transactions on multimedia"], []),
    "TCSVT": (["transactions on circuits and systems for video"], []),
    "TNNLS": (["transactions on neural networks and learning systems"], []),
    "TMI": (["transactions on medical imaging"], []),
    "MICCAI": (["medical image computing", "lecture notes in computer science"], []),
    "MIA": (["medical image analysis"], []),
    "ICASSP": (["acoustics, speech and signal processing", "icassp"], []),
    "INTERSPEECH": (["interspeech"], []),
    "ACM MM": (["multimedia"], []),
    "TGRS": (["transactions on geoscience and remote sensing"], []),
    "JSTARS": (["journal of selected topics in applied earth"], []),
    "IGARSS": (["international geoscience and remote sensing symposium", "igarss"], []),
    "PR": (["pattern recognition"], []),
    "ESWA": (["expert systems with applications"], []),
    "KBS": (["knowledge-based systems"], []),
    "TKDE": (["transactions on knowledge and data engineering"], []),
}
# Conference series Crossref indexes poorly or not at all; a venue mismatch
# against these is unreliable, so the venue check is skipped rather than warned.
UNINDEXED_VENUES = {"NeurIPS", "ICLR", "ICML", "AAAI", "IJCAI", "arXiv", "AISTATS", "UAI", "COLM"}

# Vocabulary a source-free domain adaptation paper title almost always carries.
# The point is not to police topic but to catch an identifier that resolved to a
# paper from a completely unrelated field - the failure mode where a plausible
# looking arXiv id turns out to be about something else entirely.
DOMAIN_TERMS = (
    "domain adaptation", "domain generalization", "domain generalisation",
    "source-free", "source free", "sourcefree", "test-time", "test time",
    "adaptation", "adapting", "adapt", "transfer learning", "distribution shift",
    "pseudo-label", "pseudo label", "self-training", "self training",
    "unsupervised", "semi-supervised", "few-shot", "zero-shot", "open-set",
    "open set", "continual", "federated", "segmentation", "detection",
    "classification", "re-identification", "reidentification", "recognition",
    "point cloud", "medical", "robust", "distribution", "shift", "target domain",
    "source model", "fine-tuning", "prompt", "vision-language", "foundation model",
    "knowledge distillation", "entropy", "contrastive", "representation",
)

UA = ("really-awesome-sfda-verifier/1.0 "
      "(+https://github.com/PrasannaPulakurthi/really-awesome-sfda)")

# - Title of the paper [`paper`](url) [`code`](url) `Venue'YY`
TITLE_RE = re.compile(r"^-\s+(?P<title>.+?)\s*\[`")
VENUE_TAG_RE = re.compile(r"`(?P<venue>[^`']+)'(?P<yy>\d{2})`")
LINK_RE = re.compile(r"\[`(?P<label>[^`]+)`\]\((?P<url>[^)]+)\)")
ARXIV_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/(?P<id>\d{4}\.\d{4,5})", re.I)
DOI_RE = re.compile(r"(?:doi\.org/|/doi/(?:abs/|full/)?)(?P<doi>10\.\d{4,9}/[^\s)\"<>\]]+)", re.I)
GITHUB_RE = re.compile(r"github\.com/(?P<owner>[\w.-]+)/(?P<repo>[\w.-]+)", re.I)
HUNK_RE = re.compile(r"^@@ -\d+(?:,\d+)? \+(?P<start>\d+)(?:,(?P<count>\d+))? @@")

CITATION_TITLE_RE = re.compile(br'<meta name="citation_title" content="([^"]+)"')


def norm(text):
    return re.sub(r"[^a-z0-9]+", " ", (text or "").lower()).strip()


def changed_lines_from_git(base, path):
    """Line numbers touched in `path` relative to `base`."""
    try:
        out = subprocess.run(
            ["git", "diff", "--unified=0", base + "...HEAD", "--", path],
            capture_output=True, text=True, check=True).stdout
    except Exception as exc:
        sys.stderr.write("git diff failed: %s\n" % exc)
        return set()
    lines = set()
    for row in out.splitlines():
        m = HUNK_RE.match(row)
        if m:
            start = int(m.group("start"))
            lines.update(range(start, start + int(m.group("count") or 1)))
    return lines


# Matches a venue tag in either the current `Venue'YY` form or the older
# (Venue YYYY) form, so a signature can be compared across the format change.
ANY_VENUE_RE = re.compile(r"`(?P<v1>[^`']+)'(?P<y1>\d{2})`|\((?P<v2>[^()]+?)\s+(?P<y2>(?:19|20)\d{2})\)")
ANY_URL_RE = re.compile(r"\((?P<url>https?://[^)\s]+)\)")
# A star badge carries a github.com link target of its own. Left in, adding a
# badge to an existing entry would look like a changed citation.
BADGE_ANY_RE = re.compile(r"\[!\[[^\]]*\]\([^)]*\)\]\([^)]*\)")
BULLET_RE = re.compile(r"^-\s+(?P<rest>.+)$")


def citation_signature(line):
    """What a citation actually asserts, independent of how it is formatted.

    Two lines with the same signature make the same factual claim, so a change
    between them is cosmetic and does not need re-verification.
    """
    m = BULLET_RE.match(line)
    if not m:
        return None
    line = BADGE_ANY_RE.sub("", line)
    m = BULLET_RE.match(line)
    if not m:
        return None
    urls = tuple(sorted(u for u in ANY_URL_RE.findall(line)
                        if "img.shields.io" not in u))
    if not urls:
        return None
    vm = ANY_VENUE_RE.search(line)
    venue = ""
    if vm:
        if vm.group("v1"):
            venue = "%s %s" % (vm.group("v1").strip(), vm.group("y1"))
        else:
            venue = "%s %s" % (vm.group("v2").strip(), vm.group("y2")[2:])
    # Title with links, tags, badges and the venue stripped, so wording is
    # compared but formatting is not. The venue must go too: in the older
    # format it sat inside the title text, and leaving it there makes every
    # entry look changed across the format migration.
    text = ANY_URL_RE.sub("", m.group("rest"))
    text = ANY_VENUE_RE.sub("", text)
    text = re.sub(r"\[[^\]]*\]|`[^`]*`|!\[[^\]]*\]", "", text)
    text = re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()
    return (text, urls, venue)


def unchanged_signatures(base, path):
    """Citation signatures present in `path` at revision `base`."""
    try:
        old = subprocess.run(["git", "show", "%s:%s" % (base, path)],
                             capture_output=True, text=True, check=True).stdout
    except Exception as exc:
        sys.stderr.write("could not read %s at %s: %s\n" % (path, base, exc))
        return set()
    sigs = set()
    for line in old.splitlines():
        sig = citation_signature(line)
        if sig:
            sigs.add(sig)
    return sigs


def fetch(url, timeout=30, accept=None):
    """Return (body, error_code).

    error_code is None on success, an HTTP status on an HTTP error, -1 on a
    transport failure. Callers must separate "no such thing" (404) from "not
    answering right now" (403/429/5xx): treating a rate limit as a dead
    resource would fail valid entries, and a verifier that cannot be trusted
    gets switched off.
    """
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    if accept:
        req.add_header("Accept", accept)
    token = os.environ.get("GITHUB_TOKEN")
    if token and "api.github.com" in url:
        req.add_header("Authorization", "Bearer " + token)
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read(), None
        except urllib.error.HTTPError as exc:
            if exc.code in (429, 500, 502, 503) and attempt < 2:
                time.sleep(3 * (attempt + 1))
                continue
            return None, exc.code
        except Exception:
            if attempt < 2:
                time.sleep(2)
                continue
            return None, -1
    return None, -1


@dataclass
class Finding:
    level: str
    entry: str
    message: str


@dataclass
class Entry:
    title: str
    venue: str
    year: int
    line_no: int
    links: dict = field(default_factory=dict)


def parse_entries(text):
    entries = []
    in_datasets = False
    in_contents = False
    for i, line in enumerate(text.splitlines(), start=1):
        if line.startswith("## "):
            # Datasets are not citations; Contents is a table of links; and the
            # Contribution section shows a format template, not a real entry.
            in_datasets = line.startswith(("## Datasets", "## Contribution"))
            in_contents = line.startswith("## Contents")
            continue
        if in_datasets or in_contents or not line.startswith("- "):
            continue
        links = {m.group("label").lower(): m.group("url") for m in LINK_RE.finditer(line)}
        if not links:
            continue
        tm = TITLE_RE.match(line)
        if not tm:
            continue
        venue, year = "", 0
        vm = VENUE_TAG_RE.search(line)
        if vm:
            venue = vm.group("venue").strip()
            year = 2000 + int(vm.group("yy"))
        entries.append(Entry(tm.group("title").strip(), venue, year, i, links))
    return entries


def _arxiv_from_html(arxiv_id):
    raw, err = fetch("https://arxiv.org/abs/%s" % arxiv_id)
    if raw:
        m = CITATION_TITLE_RE.search(raw)
        if m:
            title = html.unescape(m.group(1).decode("utf-8", "replace"))
            return " ".join(title.split()), "ok"
        return None, "unchecked"
    return (None, "missing") if err == 404 else (None, "unchecked")


def _arxiv_from_datacite(arxiv_id):
    raw, err = fetch("https://api.datacite.org/dois/10.48550%%2FarXiv.%s" % arxiv_id,
                     accept="application/json")
    if raw:
        try:
            attrs = json.loads(raw)["data"]["attributes"]
            return " ".join(attrs["titles"][0]["title"].split()), "ok"
        except Exception:
            return None, "unchecked"
    return (None, "missing") if err == 404 else (None, "unchecked")


def resolve_arxiv(arxiv_id):
    """Resolve an arXiv id against more than one source.

    No single source is dependable from a shared CI address - the arXiv API in
    particular rate-limits cloud runners hard. Only a positive denial counts as
    'missing'; silence counts as 'unchecked' and never as success.
    """
    saw_missing = False
    for resolver in (_arxiv_from_html, _arxiv_from_datacite):
        title, status = resolver(arxiv_id)
        if status == "ok":
            return title, "ok"
        if status == "missing":
            saw_missing = True
    return None, ("missing" if saw_missing else "unchecked")


def crossref_by_doi(doi):
    raw, _ = fetch("https://api.crossref.org/works/" + urllib.parse.quote(doi, safe=""),
                   accept="application/json")
    if not raw:
        return None, None, None
    try:
        msg = json.loads(raw)["message"]
    except Exception:
        return None, None, None
    return _crossref_fields(msg)


def crossref_by_title(title):
    """Look a paper up by title, skipping non-article records.

    Crossref registers supplementary material as its own record, with a title
    derived from the paper's. Those rank highly and carry no venue, so taking
    the first hit blindly can match a supplementary PDF and conclude the paper
    has no venue. Only real works are considered.
    """
    raw, _ = fetch("https://api.crossref.org/works?rows=5"
                   "&select=title,container-title,issued,type"
                   "&query.bibliographic=" + urllib.parse.quote(title),
                   accept="application/json")
    if not raw:
        return None, None, None
    try:
        items = json.loads(raw)["message"]["items"]
    except Exception:
        return None, None, None
    for it in items:
        if it.get("type") == "component":
            continue
        return _crossref_fields(it)
    return None, None, None


def _crossref_fields(msg):
    title = (msg.get("title") or [None])[0]
    container = (msg.get("container-title") or [None])[0]
    year = None
    for key in ("published-print", "published-online", "issued"):
        parts = msg.get(key, {}).get("date-parts") or []
        if parts and parts[0] and parts[0][0]:
            year = int(parts[0][0])
            break
    return (" ".join(title.split()) if title else None), container, year


PROCEEDINGS_HOSTS = ("openaccess.thecvf.com", "proceedings.mlr.press",
                     "papers.nips.cc", "proceedings.neurips.cc",
                     "ecva.net", "ojs.aaai.org", "ijcai.org")
# openaccess.thecvf.com/content/CVPR2022/... and the older
# openaccess.thecvf.com/content_CVPR_2020/... both name the venue and year.
CVF_URL_RE = re.compile(r"thecvf\.com/content[_/](?P<venue>[A-Za-z]+)_?(?P<year>(?:19|20)\d{2})", re.I)
CITATION_DATE_RE = re.compile(br'<meta name="citation_(?:publication_date|date)" content="(\d{4})')
TRAILING_ACRONYM_RE = re.compile(r"\s*\([^()]{1,24}\)\s*$")


def strip_trailing_acronym(title):
    """Remove a trailing model name, e.g. 'Contrastive TTA (AdaContrast)'.

    Entries often append the method's short name, which no bibliographic record
    carries, so it has to go before any title comparison.
    """
    return TRAILING_ACRONYM_RE.sub("", title).strip()


def resolve_proceedings(url):
    """Return (title, venue, year, status) from an official proceedings page.

    These pages publish citation metadata in their head. status is 'ok',
    'missing' when the page is gone, or 'unchecked' when it cannot be read.
    """
    raw, err = fetch(url)
    if not raw:
        return None, None, None, ("missing" if err == 404 else "unchecked")
    m = CITATION_TITLE_RE.search(raw)
    if not m:
        return None, None, None, "unchecked"
    title = html.unescape(m.group(1).decode("utf-8", "replace"))
    title = " ".join(title.split())

    venue = year = None
    u = CVF_URL_RE.search(url)
    if u:
        venue = u.group("venue").upper()
        year = int(u.group("year"))
    else:
        d = CITATION_DATE_RE.search(raw)
        if d:
            year = int(d.group(1))
    return title, venue, year, "ok"


# icml.cc, neurips.cc and iclr.cc publish a virtual-site page per paper. They
# carry no citation metadata, but the URL states the year and the page title is
# "<CONF> Poster <paper title>", which is enough to confirm both. Crossref does
# not index PMLR, so for ICML this is often the only machine-readable source.
CONF_SITE_RE = re.compile(r"(?P<conf>icml|neurips|iclr)\.cc/virtual/(?P<year>(?:19|20)\d{2})/", re.I)
HTML_TITLE_RE = re.compile(br"<title>\s*(?P<title>[^<]{3,300}?)\s*</title>", re.I | re.S)
CONF_PREFIX_RE = re.compile(r"^(ICML|NeurIPS|ICLR)\s+(Poster|Oral|Spotlight|Session)\s+", re.I)
CONF_NAMES = {"icml": "ICML", "neurips": "NeurIPS", "iclr": "ICLR"}


def resolve_conference_site(url):
    """Return (title, venue, year, status) from a conference virtual-site page."""
    m = CONF_SITE_RE.search(url)
    if not m:
        return None, None, None, "unchecked"
    raw, err = fetch(url)
    if not raw:
        return None, None, None, ("missing" if err == 404 else "unchecked")
    tm = HTML_TITLE_RE.search(raw)
    if not tm:
        return None, None, None, "unchecked"
    title = html.unescape(tm.group("title").decode("utf-8", "replace"))
    title = CONF_PREFIX_RE.sub("", " ".join(title.split())).strip()
    if not title:
        return None, None, None, "unchecked"
    return title, CONF_NAMES[m.group("conf").lower()], int(m.group("year")), "ok"


def check_github(owner, repo):
    """Return (stars, status) where status is 'ok', 'missing' or 'unchecked'."""
    raw, err = fetch("https://api.github.com/repos/%s/%s" % (owner, repo))
    if raw:
        try:
            return int(json.loads(raw).get("stargazers_count", 0)), "ok"
        except Exception:
            return None, "unchecked"
    if err == 404:
        return None, "missing"
    return None, "unchecked"


def looks_like_sfda(title, entry_title=""):
    """Does this resolved title plausibly belong in this list?

    Guards against an identifier resolving to a paper from an unrelated field.
    A title match against the entry settles it regardless of vocabulary.
    """
    t = (title or "").lower()
    if any(term in t for term in DOMAIN_TERMS):
        return True
    a, b = norm(title), norm(entry_title)
    if not a or not b:
        return False
    shared = set(a.split()) & set(b.split())
    return len(shared) >= max(3, len(b.split()) // 3)


def venue_matches(venue, container):
    """True, False, or None when the venue has no pattern to check against."""
    pats = VENUE_PATTERNS.get(venue)
    if not pats or not container:
        return None
    accept, reject = pats
    c = container.lower()
    if any(r in c for r in reject):
        return False
    return any(a in c for a in accept)


def verify(entries, delay=1.0, check_venues=True, progress_every=0):
    """Check each entry, optionally reporting progress to stderr as it goes.

    A full sweep takes minutes. Without progress output there is no way to
    distinguish a slow run from a stalled one, and no way to see problems
    accumulating before the end.
    """
    findings = []
    seen = {}
    total = len(entries)
    for idx, e in enumerate(entries, start=1):
        label = "%s (line %d)" % (e.title[:58], e.line_no)
        if progress_every and (idx % progress_every == 0 or idx == total):
            counts = {}
            for f in findings:
                counts[f.level] = counts.get(f.level, 0) + 1
            sys.stderr.write(
                "PROGRESS %d/%d | %d fail, %d warn, %d unverified\n"
                % (idx, total, counts.get("fail", 0), counts.get("warn", 0),
                   counts.get("unchecked", 0)))
            sys.stderr.flush()

        paper_url = e.links.get("paper") or e.links.get("arxiv") or e.links.get("pdf")
        if not paper_url:
            findings.append(Finding("warn", label, "no paper or arxiv link"))
            continue

        key = paper_url.rstrip("/")
        if key in seen and seen[key] != e.title:
            findings.append(Finding("warn", label,
                "link duplicates entry '%s'" % seen[key][:48]))
        seen.setdefault(key, e.title)

        resolved_title = None

        am = ARXIV_RE.search(paper_url) or (
            ARXIV_RE.search(e.links.get("arxiv", "")) if e.links.get("arxiv") else None)
        if am:
            title, status = resolve_arxiv(am.group("id"))
            time.sleep(delay)
            if status == "missing":
                findings.append(Finding("fail", label,
                    "arXiv id %s does not exist" % am.group("id")))
            elif status == "unchecked":
                findings.append(Finding("unchecked", label,
                    "arXiv id %s could not be resolved - NOT verified" % am.group("id")))
            else:
                resolved_title = title
                findings.append(Finding("info", label, "resolved: " + title))
                if not looks_like_sfda(title, e.title):
                    findings.append(Finding("warn", label,
                        "resolved title looks unrelated to this list - check the "
                        "identifier: '%s'" % title))

        dm = DOI_RE.search(paper_url)
        if dm and check_venues:
            title, container, year = crossref_by_doi(dm.group("doi").rstrip("."))
            time.sleep(delay)
            if title:
                resolved_title = resolved_title or title
                if container:
                    findings.append(Finding("info", label,
                        "venue record: %s (%s)" % (container, year)))
                    ok = venue_matches(e.venue, container)
                    if ok is False:
                        findings.append(Finding("warn", label,
                            "entry says %s but the record says '%s'" % (e.venue, container)))
                if year and e.year and abs(year - e.year) > 1:
                    findings.append(Finding("warn", label,
                        "entry says %d but the record says %d" % (e.year, year)))

        elif check_venues:
            # No arXiv id and no DOI in the URL. Most links of this kind are
            # proceedings pages (CVF, IEEE Xplore, Springer, MLR) that carry no
            # identifier in the path, so the paper is looked up by its title
            # instead. Without this branch such entries were checked by nothing
            # at all and still counted as passing, which is the worst outcome a
            # verifier can produce.
            lookup = strip_trailing_acronym(resolved_title or e.title)

            # A conference's own virtual site is a primary source, and for ICML
            # it is often the only machine-readable one, since Crossref does not
            # index PMLR.
            if CONF_SITE_RE.search(paper_url):
                ctitle, cvenue, cyear, cstatus = resolve_conference_site(paper_url)
                time.sleep(delay)
                if cstatus == "ok":
                    resolved_title = resolved_title or ctitle
                    findings.append(Finding("info", label, "resolved: " + ctitle))
                    if norm(strip_trailing_acronym(e.title)) != norm(ctitle):
                        findings.append(Finding("warn", label,
                            "entry title differs from the conference page: '%s'" % ctitle))
                    if cvenue and e.venue and cvenue.upper() != e.venue.upper():
                        findings.append(Finding("warn", label,
                            "entry says %s but the page is on the %s site"
                            % (e.venue, cvenue)))
                    if cyear and e.year and abs(cyear - e.year) > 1:
                        findings.append(Finding("warn", label,
                            "entry says %d but the page says %d" % (e.year, cyear)))
                    continue

            # An official proceedings page is a primary source and states the
            # title outright, so prefer it to a fuzzy bibliographic search.
            if any(h in paper_url for h in PROCEEDINGS_HOSTS):
                ptitle, pvenue, pyear, pstatus = resolve_proceedings(paper_url)
                time.sleep(delay)
                if pstatus == "missing":
                    findings.append(Finding("fail", label,
                        "proceedings page does not exist: %s" % paper_url))
                    continue
                if pstatus == "ok":
                    resolved_title = resolved_title or ptitle
                    findings.append(Finding("info", label, "resolved: " + ptitle))
                    if norm(strip_trailing_acronym(e.title)) != norm(ptitle):
                        findings.append(Finding("warn", label,
                            "entry title differs from the proceedings page: '%s'"
                            % ptitle))
                    if pvenue and e.venue and pvenue != e.venue.upper():
                        findings.append(Finding("warn", label,
                            "entry says %s but the proceedings URL says %s"
                            % (e.venue, pvenue)))
                    if pyear and e.year and abs(pyear - e.year) > 1:
                        findings.append(Finding("warn", label,
                            "entry says %d but the page says %d" % (e.year, pyear)))
                    continue

            found, container, year = crossref_by_title(lookup)
            time.sleep(delay)
            if found and norm(found) == norm(lookup):
                resolved_title = resolved_title or found
                if container:
                    ok = venue_matches(e.venue, container)
                    if ok is False:
                        findings.append(Finding("warn", label,
                            "entry says %s but the record says '%s' (%s)"
                            % (e.venue, container, year)))
                    else:
                        findings.append(Finding("info", label,
                            "venue record: %s (%s)" % (container, year)))
                if year and e.year and abs(year - e.year) > 1:
                    findings.append(Finding("warn", label,
                        "entry says %d but the record says %d" % (e.year, year)))
            elif not resolved_title:
                # Nothing identified this paper. Say so rather than stay silent.
                findings.append(Finding("unchecked", label,
                    "no identifier and no title match - NOT verified"))

        code_url = e.links.get("code")
        if code_url:
            gm = GITHUB_RE.search(code_url)
            if gm:
                repo = gm.group("repo").rstrip("/")
                stars, status = check_github(gm.group("owner"), repo)
                time.sleep(delay)
                if status == "missing":
                    findings.append(Finding("fail", label,
                        "repository %s/%s does not exist" % (gm.group("owner"), repo)))
                elif status == "unchecked":
                    findings.append(Finding("info", label,
                        "repository not checked (rate limited)"))
    return findings


def main():
    # Paper titles contain mathematical symbols and accented characters. On a
    # console whose default encoding cannot represent them (cp1252 on Windows),
    # printing a result raises UnicodeEncodeError and kills the run partway -
    # leaving partial output that reads like a clean pass. Force UTF-8 so a
    # stray glyph cannot silently truncate an audit.
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except AttributeError:  # Python < 3.7
            pass

    ap = argparse.ArgumentParser()
    ap.add_argument("--readme", default="README.md")
    ap.add_argument("--only")
    ap.add_argument("--diff-base")
    ap.add_argument("--no-venues", action="store_true")
    ap.add_argument("--delay", type=float, default=1.0)
    ap.add_argument("--markdown", action="store_true")
    ap.add_argument("--progress-every", type=int, default=0,
                    help="report progress to stderr every N entries")
    ap.add_argument("--limit", type=int, default=0,
                    help="verify at most N entries (0 = no limit)")
    args = ap.parse_args()

    text = open(args.readme, encoding="utf-8").read()
    entries = parse_entries(text)

    if args.only:
        entries = [e for e in entries if args.only.lower() in e.title.lower()]
    if args.diff_base:
        # Select by what the citation asserts, not by which lines moved. A
        # reformatting pass changes every line while changing no citation, and
        # re-verifying the whole list for that is slow enough that people
        # eventually turn the check off.
        known = unchanged_signatures(args.diff_base, args.readme)
        lines = text.splitlines()
        keep = []
        for e in entries:
            sig = citation_signature(lines[e.line_no - 1])
            if sig is None or sig not in known:
                keep.append(e)
        skipped = len(entries) - len(keep)
        if skipped:
            sys.stderr.write("%d entries unchanged since %s - not re-verified\n"
                             % (skipped, args.diff_base[:8]))
        entries = keep
    if args.limit:
        entries = entries[:args.limit]

    if not entries:
        print("No entries to verify.")
        return 0

    sys.stderr.write("Verifying %d entries...\n" % len(entries))
    findings = verify(entries, delay=args.delay, check_venues=not args.no_venues,
                      progress_every=args.progress_every)

    fails = [f for f in findings if f.level == "fail"]
    warns = [f for f in findings if f.level == "warn"]
    infos = [f for f in findings if f.level == "info"]
    unchecked = [f for f in findings if f.level == "unchecked"]

    if args.markdown:
        print("## Citation verification\n")
        print("Checked **%d** entries: **%d** failures, **%d** warnings, "
              "**%d** not verified.\n" % (len(entries), len(fails), len(warns), len(unchecked)))
        for heading, group, note in (
                ("Not verified", unchecked,
                 "No source could confirm these, so this run proves nothing about them."),
                ("Failures (must fix)", fails, ""),
                ("Warnings (review)", warns, "")):
            if group:
                print("### %s\n" % heading)
                if note:
                    print(note + "\n")
                for f in group:
                    print("- **%s** - %s" % (f.entry, f.message))
                print("")
        if infos:
            print("<details><summary>Resolved metadata</summary>\n")
            for f in infos:
                print("- **%s** - %s" % (f.entry, f.message))
            print("\n</details>")
    else:
        for f in unchecked:
            print("UNVERIFIED  %s: %s" % (f.entry, f.message))
        for f in fails:
            print("FAIL  %s: %s" % (f.entry, f.message))
        for f in warns:
            print("WARN  %s: %s" % (f.entry, f.message))
        for f in infos:
            print("info  %s: %s" % (f.entry, f.message))
        print("\n%d entries | %d failures | %d warnings | %d not verified"
              % (len(entries), len(fails), len(warns), len(unchecked)))

    # An entry nobody could confirm is not a pass. Reporting it as one turns a
    # verification step into false assurance, which is worse than having none.
    return 1 if (fails or unchecked) else 0


if __name__ == "__main__":
    sys.exit(main())
