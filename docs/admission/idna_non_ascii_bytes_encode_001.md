# Admission checklist - idna_non_ascii_bytes_encode_001

Facts below are machine-derived from the upstream Git objects and from this
repository's CI. **Tick boxes and initials are left blank on purpose**: this file
records what was measured, not that a person has reviewed it. Per the protocol,
automation cannot sign these sections.

```
Case id:       idna_non_ascii_bytes_encode_001
Upstream:      kjd/idna
Buggy commit:  522c0ebe02d8bd09039dd593e7c152ab5a1d26dd
Fixed commit:  e00ed2854c5203be201940f4029a747684594409
Builder: ______________________   Build date: _________
```

## 1. Provenance
- [ ] Full buggy and fixed SHAs recorded; object format recorded.
- [ ] Buggy is an ancestor of fixed (ancestry proof recorded).
- [ ] Buggy and fixed tree SHAs recorded.
- [ ] Parent lists recorded; interval matches the historical-interval policy.
- [ ] Selected commit is not a superseded intermediate (or is labelled and justified).

> Measured: object format `sha1`; buggy tree `30a882a7cd6aa63fb19e6c4661f89c5794bfdc71`;
> fixed tree `b2220c6951105614605aa4c3811a01b4e10fba98`. Ancestry is re-proved on every rebuild by
> `scripts/rebuild_pack.py` (`git merge-base --is-ancestor`), which CI runs.

Provenance verified by: __________________  Date: __________

## 2. Historical evidence
- [ ] Issue and/or PR URLs recorded, with their relationship to the fixed commit.
- [ ] A maintainer-grounded statement establishes the behavior as a defect.
- [ ] The defect is not inferred from the commit message or PR title alone.

> Recorded: issue https://github.com/kjd/idna/issues/119
> PR https://github.com/kjd/idna/commit/e00ed2854c5203be201940f4029a747684594409
> Defect evidence: Issue #119 and commit e00ed28 ("Raise IDNAError on non-ASCII A-label") report that encode leaked UnicodeDecodeError for a non-ASCII byte string. test_encode is extended with that input and expects IDNAError.

Historical evidence verified by: __________________  Date: __________

## 3. Regression reproduction
- [ ] Targeted regression test path and function recorded.
- [ ] Buggy run fails for the intended behavioral assertion; failing assertion recorded.
- [ ] Fixed run passes.
- [ ] Exact Python and dependency versions and the exact command recorded.
- [ ] Reproduction label recorded.

> Measured: `tests/test_idna.py` :: `test_encode`.
> CI verdict **VERIFIED** - baseline_fails=pass, reference_passes=pass,
> deterministic=pass across 3 runs.
> Environment: Python 3.11, pytest 8.3.5, network none.

Regression reproduction verified by: __________________  Date: __________

## 4. Path classification
- [ ] Complete diff name-status recorded; every path classified.
- [ ] No unclassified generated/doc/config path.
- [ ] Selectors and tests root recorded.

> Measured changed paths: `idna/core.py`, `tests/test_idna.py`
> Selectors: `idna`; tests root `tests`.

Path classification verified by: __________________  Date: __________

## 5. Execution environment
- [ ] Networking disabled. No credentials, external services, or submodules.
- [ ] No third-party pytest plugin beyond the pinned image.
- [ ] Every runtime dependency pinned in the image lock and justified.

> Measured: image `realfix-pilot:2`, network `none`, plugins `none`,
> submodules `none`, extra deps: none.

Execution environment verified by: __________________  Date: __________

## 6. Task-surface leakage
- [ ] Ground-truth vocabulary checked against tests, comments, filenames, patch wording.
- [ ] Scoring fields paraphrase rather than copy distinctive terms.
- [ ] Strict contamination lint passes.
- [ ] Leakage risk recorded low / medium / high with justification.
- [ ] No upstream comment or test deleted or rewritten to pass lint.

> Measured: `arena lint-cases --strict` passes on this pack in CI.
> Analysis: Reviewer-visible surfaces expose encode/decode vocabulary (bytes.decode('ascii') in encode; the covering method is test_encode). Ground truth paraphrases the defect ("raw codec error", "bytes argument") and is checked by strict contamination lint.
> Risk label is a judgment and is left for the reviewer: ____________

Task-surface leakage verified by: __________________  Date: __________

## 6b. Historical exposure
- [ ] Upstream fix date, issue/PR public date, benchmark publication date recorded.
- [ ] Exposure risk recorded with justification.
- [ ] Collection-vs-model-release relationship recorded.
- [ ] Retrieval-during-evaluation recorded.

> Measured: upstream fix date `2022-04-27`, read from the commit object by the
> importer and carried in the case's `origin` block.
> Risk label is a judgment and is left for the reviewer: ____________

Historical exposure verified by: __________________  Date: __________

## 7. Mutation
- [ ] Mutation run recorded with limit and viable-mutant count.
- [ ] Kill rate recorded, or "zero viable mutants" recorded explicitly.
- [ ] Zero mutation evidence not presented as a measured kill rate.
- [ ] No mutants manufactured, no hidden tests added.

> Measured on `realfix-pilot:2` at limit 25: **76% kill on 25 mutants**.

Mutation verified by: __________________  Date: __________

## 8. Licensing
- [ ] Upstream SPDX and license-file blob SHAs at the pinned commit recorded.
- [ ] Exact pinned license texts vendored (all files for dual licences).
- [ ] NOTICE / AUTHORS / data-licence requirements checked.
- [ ] Per-case third-party notice recorded; nothing relicensed.

> Measured SPDX: `BSD-3-Clause`
  - `LICENSE.md` blob `b6f87326ffb36158c33f5e6dc9d6175262050cea`
> Each vendored file was hashed and matches the upstream blob at the pinned commit.
> Blobs identical at both commits: True.

Licensing verified by: __________________  Date: __________

## 9. Deterministic rebuild
- [ ] Two consecutive rebuilds produce byte-identical content and `pack.sha256`.
- [ ] Licence and notice files are covered by `pack.sha256`.

> Measured: CI rebuilds every case from its upstream clone and fails the build unless
> `git diff --exit-code` on the pack is empty.

Deterministic rebuild verified by: __________________  Date: __________

## 10. Control behavior
- [ ] `reference-patch` validates the case.
- [ ] Bad, malformed and no-patch controls do not validate it.
- [ ] Keyword-gamer obtains no validated repair.

> Measured: CI's Controls step asserts reference-patch validates all cases and that
> `control:bad_patch`, `control:malformed_patch`, `control:detects_no_patch` and
> `control:keyword_gamer` validate none.

Control behavior verified by: __________________  Date: __________

## 11. Final admission decision

Decision (accepted / hold / rejected / deprecated): ______________
Acceptance level (provisional / paper-grade): ______________
Builder: __________________  Date: __________
Independent reviewer (required for paper-grade; a real person, not the builder
or any automation): __________________  Date: __________
