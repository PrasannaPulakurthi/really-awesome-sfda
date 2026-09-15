# Contributing

Thanks for helping keep this list useful and accurate.

This list is **comprehensive by design**. It aims to cover source-free domain
adaptation broadly rather than to select an elite subset, so a paper is not
rejected for appearing at a smaller venue. What it is strict about is whether
the citation is *correct*.

## Inclusion criteria

1. **Relevant to SFDA or an adjacent setting** — source-free adaptation,
   test-time adaptation, and the extensions covered in the existing sections
   (open-set, continual, federated, multi-source, active, cross-modal).
2. **Accurately cited** — the venue, year and links must match the actual
   record. This is the part that is enforced.
3. **Not already listed.** Check before opening a PR.

Preprints are welcome and tagged `arXiv`. If a preprint later appears at a
venue, updating its entry is a valuable contribution in itself.

## Entry format

One line per paper, in this exact shape:

```
- Title of the Paper (Venue YYYY) [[paper](url)] [[code](url)]
```

- Use the **published venue** where one exists, otherwise `arXiv`.
- Link labels in use: `paper`, `arxiv`, `code`, `project`, `pdf`, `dataset`.
- Where a repository exists, include `code` — it is the single most useful
  field in the list for a reader trying to build on the work.
- Order within a section is newest first.

## Before you open a PR

- [ ] Verify the venue and year from a primary source: the publisher page, the
      proceedings listing, or the arXiv abstract's Comments field.
- [ ] Click the links. A dead or redirected link is worth reporting on its own.
- [ ] Confirm the paper is not already listed under another section.
- [ ] Run the verifier on your addition (below).

## Automated verification

Every pull request touching `README.md` runs `scripts/verify_citations.py`,
which resolves the identifiers in your changed entries and posts the result as a
comment.

Run it yourself first:

```bash
python scripts/verify_citations.py --only "part of your title"
```

It reports at four levels:

- **Failure** blocks the merge: an identifier does not exist, or a linked
  repository is gone.
- **Not verified** also blocks: no source could confirm the identifier, so the
  run proves nothing about it. Silence is not success.
- **Warning** asks for review: a venue or year disagreeing with the record, a
  duplicate link, a resolved title that looks unrelated.
- **Info** is resolved metadata, printed so a reviewer can compare the fetched
  title against the entry at a glance.

A check that could not run — a rate limit, a service outage — is reported as
skipped and never silently as a pass.

It cannot check whether a title fairly represents the paper. That is still a
person reading it.

## Corrections

Wrong venue, wrong year, dead link, duplicated entry, mis-attributed work:
please open an issue or PR. Corrections are the most valuable contribution to a
list like this, and more welcome than additions.
