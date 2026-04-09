# Admission checklist - packaging_infinity_self_comparison_001

Facts below are machine-derived from the upstream Git objects and from this
repository's CI. **Tick boxes and initials are left blank on purpose**: this file
records what was measured, not that a person has reviewed it. Per the protocol,
automation cannot sign these sections.

```
Case id:       packaging_infinity_self_comparison_001
Upstream:      pypa/packaging
Buggy commit:  4339d3a0028348e21863664e6022e3cff20c3411
Fixed commit:  f8f16338e10d5d509ea2a29e0f0cf56baf4be565
Builder: ______________________   Build date: _________
```

## 1. Provenance
- [ ] Full buggy and fixed SHAs recorded; object format recorded.
- [ ] Buggy is an ancestor of fixed (ancestry proof recorded).
- [ ] Buggy and fixed tree SHAs recorded.
- [ ] Parent lists recorded; interval matches the historical-interval policy.
- [ ] Selected commit is not a superseded intermediate (or is labelled and justified).

> Measured: object format `sha1`; buggy tree `c9c93e7d1c812bc7a99e35f2825ec360d2034b73`;
> fixed tree `047f8d789e3cfa3972a2d3107b320096e488a3d5`. Ancestry is re-proved on every rebuild by
> `scripts/rebuild_pack.py` (`git merge-base --is-ancestor`), which CI runs.

Provenance verified by: __________________  Date: __________

## 2. Historical evidence
- [ ] Issue and/or PR URLs recorded, with their relationship to the fixed commit.
- [ ] A maintainer-grounded statement establishes the behavior as a defect.
- [ ] The defect is not inferred from the commit message or PR title alone.

> Recorded: issue https://github.com/pypa/packaging/pull/1093
> PR https://github.com/pypa/packaging/pull/1093
> Defect evidence: PR #1093 ("Fix incorrect self-comparison for InfinityType and NegativeInfinityType") reports that the version sentinels compared as unordered against themselves: Infinity < Infinity was true and Infinity <= Infinity was false. The PR adds regression tests that require a sentinel to compare equal-or-

Historical evidence verified by: __________________  Date: __________

## 3. Regression reproduction
- [ ] Targeted regression test path and function recorded.
- [ ] Buggy run fails for the intended behavioral assertion; failing assertion recorded.
- [ ] Fixed run passes.
- [ ] Exact Python and dependency versions and the exact command recorded.
- [ ] Reproduction label recorded.

> Measured: `tests/test_structures.py` :: `test_infinity_self_comparison`.
> CI verdict **VERIFIED** - baseline_fails=pass, reference_passes=pass,
> deterministic=pass across 3 runs.
> Environment: Python 3.11, pytest 8.3.5, network none.

Regression reproduction verified by: __________________  Date: __________

## 4. Path classification
- [ ] Complete diff name-status recorded; every path classified.
- [ ] No unclassified generated/doc/config path.
- [ ] Selectors and tests root recorded.

> Measured changed paths: `src/packaging/_structures.py`, `tests/test_structures.py`
> Selectors: `src/packaging`; tests root `tests`.

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
> Analysis: Reviewer-visible surfaces expose InfinityType comparison vocabulary (the buggy methods always returned True/False without an identity guard; the new tests are named for self-comparison). Ground truth paraphrases the defect ("sentinel identity", "same sentinel") and is checked by strict contamination lint.
> Risk label is a judgment and is left for the reviewer: ____________

Task-surface leakage verified by: __________________  Date: __________

## 6b. Historical exposure
- [ ] Upstream fix date, issue/PR public date, benchmark publication date recorded.
- [ ] Exposure risk recorded with justification.
- [ ] Collection-vs-model-release relationship recorded.
- [ ] Retrieval-during-evaluation recorded.

> Measured: upstream fix date `2026-03-08`, read from the commit object by the
> importer and carried in the case's `origin` block.
> Risk label is a judgment and is left for the reviewer: ____________

Historical exposure verified by: __________________  Date: __________

## 7. Mutation
- [ ] Mutation run recorded with limit and viable-mutant count.
- [ ] Kill rate recorded, or "zero viable mutants" recorded explicitly.
- [ ] Zero mutation evidence not presented as a measured kill rate.
- [ ] No mutants manufactured, no hidden tests added.

> Measured on `realfix-pilot:2` at limit 25: **100% kill on 10 mutants**.

Mutation verified by: __________________  Date: __________

## 8. Licensing
- [ ] Upstream SPDX and license-file blob SHAs at the pinned commit recorded.
- [ ] Exact pinned license texts vendored (all files for dual licences).
- [ ] NOTICE / AUTHORS / data-licence requirements checked.
- [ ] Per-case third-party notice recorded; nothing relicensed.

> Measured SPDX: `Apache-2.0 OR BSD-2-Clause`
  - `LICENSE` blob `6f62d44e4ef733c0e713afcd2371fed7f2b3de67`
  - `LICENSE.APACHE` blob `f433b1a53f5b830a205fd2df78e2b34974656c7b`
  - `LICENSE.BSD` blob `42ce7b75c92fb01a3f6ed17eea363f756b7da582`
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
