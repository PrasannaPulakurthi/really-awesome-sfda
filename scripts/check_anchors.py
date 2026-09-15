#!/usr/bin/env python3
"""Check that every internal #anchor link in README.md resolves to a heading.

The contents block links to every section, so a renamed heading silently breaks
navigation. lychee validates external URLs but not in-document fragments, hence
this check.

Exit codes:
  0  every internal link resolves
  1  at least one broken link
"""

import io
import re
import sys


def slug(heading):
    """GitHub's heading-to-anchor transformation.

    Note that GitHub replaces each space with a single hyphen and does NOT
    collapse runs. A heading containing "&" therefore yields a double hyphen,
    because the ampersand is stripped but the spaces on either side are not.
    """
    h = heading.strip().lower()
    h = re.sub(r"[^\w\s-]", "", h)
    return h.replace(" ", "-")


def main(path="README.md"):
    text = io.open(path, encoding="utf-8").read()

    headings = []
    in_code = False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        m = re.match(r"^#{2,6}\s+(.*)$", line)
        if m:
            headings.append(slug(m.group(1)))

    # Duplicate headings get -1, -2 ... suffixes in document order.
    seen = {}
    anchors = set()
    for h in headings:
        n = seen.get(h, 0)
        anchors.add(h if n == 0 else "%s-%d" % (h, n))
        seen[h] = n + 1

    links = sorted(set(re.findall(r"\]\(#([^)]+)\)", text)))
    broken = [l for l in links if l not in anchors]

    print("%d headings, %d internal links, %d broken"
          % (len(headings), len(links), len(broken)))
    for b in broken:
        print("  broken: #%s" % b)
    if broken:
        print("\nA link points at a heading that does not exist. Either the "
              "heading was renamed or the anchor was mistyped.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "README.md"))
