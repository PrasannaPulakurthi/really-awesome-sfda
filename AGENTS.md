# AGENTS.md

Instructions for AI coding agents working in this repository.

This repo is a **curated citation list**. There is no build, no test suite and no
application code. The product is the accuracy of the claims in `README.md`.
That changes what "done" means: a plausible-looking entry is worse than no entry.

## The one rule that matters

**Never write a citation you have not verified against a primary source.**

A wrong citation here propagates into other people's bibliographies and is very
hard to undo. Every other instruction follows from this one.

### What counts as a primary source

- The publisher's page (IEEE Xplore, ScienceDirect, SpringerLink, ACM DL).
- The official proceedings listing (`openaccess.thecvf.com`,
  `proceedings.neurips.cc`, `proceedings.mlr.press`, `openreview.net`,
  `ojs.aaai.org`, `ijcai.org`).
- The arXiv abstract page, specifically its **Comments** or **Journal
  reference** field.
- A Crossref record, including its title-search endpoint
  (`api.crossref.org/works?query.bibliographic=...`), which indexes conference
  proceedings as well as journals and needs no DOI known in advance.

### What does NOT count

- **A project's own README.** Repositories routinely announce acceptance that
  never happened, or state the wrong year.
- **A search engine summary.** Useful for finding candidates, not for
  confirming facts.
- **Another awesome-list.** Errors propagate between lists; do not launder them.
- **Your own recollection.** You may well know this literature. It is not
  evidence.

### Never construct an identifier

Do not guess an arXiv id, DOI or document number from a pattern, and do not
assume a proceedings URL resolves because similar ones do. Fetch it and read the
returned title back.

This is not hypothetical. In a sibling repository, guessed identifiers resolved
to a paper on commercial bank credit risk and a paper on controllable music
generation. Both looked entirely plausible as identifiers. Always read the title
that comes back.

### When you cannot verify

Mark it, do not guess:

- Venue unconfirmed → tag the entry `arXiv` with the year.
- Cannot confirm the paper exists at all → **do not add it**, and say so in your
  PR description.

Reporting "I could not verify these six" is a good outcome. Filling them in with
confident-looking guesses is a failure, even if most turn out correct.

## Scope

This list is **comprehensive, not curated by prestige**. Do not remove an entry
because its venue is small, and do not add a venue policy. The strictness here
is about correctness, not selectivity.

An entry belongs if it concerns source-free domain adaptation or one of the
adjacent settings the list already covers, and if its citation is accurate.

## Entry format

```
- Title of the Paper (Venue YYYY) [[paper](url)] [[code](url)]
```

Use the published venue where one exists, otherwise `arXiv`. Include `code`
wherever a repository exists — it is the most useful field in the list. Keep
sections ordered newest first.

## Check your work before proposing it

```bash
python scripts/verify_citations.py --only "part of the title"
python scripts/check_anchors.py
```

The verifier prints the real title it resolved. **Read that title.** If it does
not describe the paper you think you are citing, the identifier is wrong.

Do not propose an entry whose verification you have not run, and do not silence
a failure by removing the check. If you believe a reported failure is wrong, say
so in the PR and explain why.

## Tasks that suit an agent

Well suited — mechanical and verifiable:

- Fixing broken or redirected links (confirm the new target is the same paper).
- Normalising entry formatting to the template above.
- Finding duplicate entries listed under two sections.
- Adding `code` links for papers whose repositories exist but are not linked.
- Updating a preprint's entry once it appears at a venue.
- Checking that every anchor in the contents block resolves.

Poorly suited — do not attempt autonomously:

- Writing a description of a paper you have not read.
- Bulk-importing entries from another list without verifying each one.
- Deciding an entry is out of scope and deleting it.
- Resolving a venue disagreement without fetching a primary source.

## Commit and PR conventions

- **Do not add AI attribution trailers** of any kind — no `Co-Authored-By`, no
  tool signatures.
- Commit messages: imperative mood, explaining *why* rather than only what.
- In PR descriptions, state which sources you verified against and list anything
  you could **not** verify. A PR that hides its uncertainty is harder to review
  than one that admits it.

## Repository layout

```
README.md          The list itself. The deliverable.
CONTRIBUTING.md    Human-facing contribution rules.
AGENTS.md          This file.
scripts/
  verify_citations.py   Resolves identifiers, cross-checks venues.
  check_anchors.py      Validates internal links.
.github/
  ISSUE_TEMPLATE/  Templates for additions and corrections.
  workflows/       Link checking and citation verification.
```

There is nothing to build or run. To validate changes, check that the Markdown
renders and that both scripts pass.
