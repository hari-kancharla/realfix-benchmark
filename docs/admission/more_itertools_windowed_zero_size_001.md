# Admission checklist - more_itertools_windowed_zero_size_001

Facts in the `>` blocks are derived from the upstream Git objects and from this
repository's CI. The builder has reviewed them and signed the sections below.

**The independent-reviewer line is deliberately unsigned** - the
protocol requires a second real person for that, and no second reviewer has looked at
this case. The case is therefore *provisionally* accepted, not paper-grade.

```
Case id:       more_itertools_windowed_zero_size_001
Upstream:      more-itertools/more-itertools
Buggy commit:  e4d2a4a2a97246a73856754b2c4866d7f41d4875
Fixed commit:  71b46b06fb48abcd2f7a26d74c148a650d340386
Builder: Hari Kancharla            Build date: 2026-04-09
```

## 1. Provenance
- [x] Full buggy and fixed SHAs recorded; object format recorded.
- [x] Buggy is an ancestor of fixed (ancestry proof recorded).
- [x] Buggy and fixed tree SHAs recorded.
- [x] Parent lists recorded; interval matches the historical-interval policy.
- [x] Selected commit is not a superseded intermediate (or is labelled and justified).

> Measured: object format `sha1`; buggy tree `1081ad92ff6ff7eed4a85cf48a988bb3f5c4ea64`;
> fixed tree `2806161a08e038aee3e636ce2bc53a8a9e34cfc6`. Ancestry is re-proved on every rebuild by
> `scripts/rebuild_pack.py` (`git merge-base --is-ancestor`), which CI runs.

Provenance verified by: Hari Kancharla   Date: 2026-04-09

## 2. Historical evidence
- [x] Issue and/or PR URLs recorded, with their relationship to the fixed commit.
- [x] A maintainer-grounded statement establishes the behavior as a defect.
- [x] The defect is not inferred from the commit message or PR title alone.

> Recorded: issue https://github.com/more-itertools/more-itertools/issues/1057
> PR https://github.com/more-itertools/more-itertools/pull/1139
> Defect evidence: Issue #1057 ("Why does windowed(xs, 0) return a range of 1 empty tuple?") shows that windowed() with size zero yielded a single empty tuple rather than rejecting the size. PR #1139 (authored by Raymond Hettinger) changes the guard so a size of zero is rejected together with negative sizes.


Historical evidence verified by: Hari Kancharla   Date: 2026-04-09

## 3. Regression reproduction
- [x] Targeted regression test path and function recorded.
- [x] Buggy run fails for the intended behavioral assertion; failing assertion recorded.
- [x] Fixed run passes.
- [x] Exact Python and dependency versions and the exact command recorded.
- [x] Reproduction label recorded.

> Measured: `tests/test_more.py` :: `test_invalid_n`.
> CI verdict **VERIFIED** - baseline_fails=pass, reference_passes=pass,
> deterministic=pass across 3 runs.
> Environment: Python 3.11, pytest 8.3.5, network none.

Regression reproduction verified by: Hari Kancharla   Date: 2026-04-09

## 4. Path classification
- [x] Complete diff name-status recorded; every path classified.
- [x] No unclassified generated/doc/config path.
- [x] Selectors and tests root recorded.

> Measured changed paths: `more_itertools/more.py`, `tests/test_more.py`
> Selectors: `more_itertools`; tests root `tests`.

Path classification verified by: Hari Kancharla   Date: 2026-04-09

## 5. Execution environment
- [x] Networking disabled. No credentials, external services, or submodules.
- [x] No third-party pytest plugin beyond the pinned image.
- [x] Every runtime dependency pinned in the image lock and justified.

> Measured: image `realfix-pilot:2`, network `none`, plugins `none`,
> submodules `none`, extra deps: none.

Execution environment verified by: Hari Kancharla   Date: 2026-04-09

## 6. Task-surface leakage
- [x] Ground-truth vocabulary checked against tests, comments, filenames, patch wording.
- [x] Scoring fields paraphrase rather than copy distinctive terms.
- [x] Strict contamination lint passes.
- [x] Leakage risk recorded low / medium / high with justification.
- [x] No upstream comment or test deleted or rewritten to pass lint.

> Measured: `arena lint-cases --strict` passes on this pack in CI.
> Analysis: Reviewer-visible surfaces expose invalid-size vocabulary. The regression test name is generic (test_invalid_n). Ground truth paraphrases the defect ("zero-length window", "argument domain check") and is checked by strict contamination lint.

> Leakage risk: **low** - ground-truth wording paraphrases the defect and strict contamination lint passes.

Task-surface leakage verified by: Hari Kancharla   Date: 2026-04-09

## 6b. Historical exposure
- [x] Upstream fix date, issue/PR public date, benchmark publication date recorded.
- [x] Exposure risk recorded with justification.
- [x] Collection-vs-model-release relationship recorded.
- [x] Retrieval-during-evaluation recorded.

> Measured: upstream fix date `2026-03-31`, read from the commit object by the
> importer and carried in the case's `origin` block.
> Exposure risk: **low** - the fix became public on 2026-03-31, recently enough that it may postdate the evaluated model's cutoff; this is a date relationship, not proof of non-exposure.

Historical exposure verified by: Hari Kancharla   Date: 2026-04-09

## 7. Mutation
- [x] Mutation run recorded with limit and viable-mutant count.
- [x] Kill rate recorded, or "zero viable mutants" recorded explicitly.
- [x] Zero mutation evidence not presented as a measured kill rate.
- [x] No mutants manufactured, no hidden tests added.

> Measured on `realfix-pilot:2` at limit 25: **100% kill on 25 mutants**.

Mutation verified by: Hari Kancharla   Date: 2026-04-09

## 8. Licensing
- [x] Upstream SPDX and license-file blob SHAs at the pinned commit recorded.
- [x] Exact pinned license texts vendored (all files for dual licences).
- [x] NOTICE / AUTHORS / data-licence requirements checked.
- [x] Per-case third-party notice recorded; nothing relicensed.

> Measured SPDX: `MIT`
  - `LICENSE` blob `0a523bece3e50519653c4d7a38399baa487fefa1`
> Each vendored file was hashed and matches the upstream blob at the pinned commit.
> Blobs identical at both commits: True.

Licensing verified by: Hari Kancharla   Date: 2026-04-09

## 9. Deterministic rebuild
- [x] Two consecutive rebuilds produce byte-identical content and `pack.sha256`.
- [x] Licence and notice files are covered by `pack.sha256`.

> Measured: CI rebuilds every case from its upstream clone and fails the build unless
> `git diff --exit-code` on the pack is empty.

Deterministic rebuild verified by: Hari Kancharla   Date: 2026-04-09

## 10. Control behavior
- [x] `reference-patch` validates the case.
- [x] Bad, malformed and no-patch controls do not validate it.
- [x] Keyword-gamer obtains no validated repair.

> Measured: CI's Controls step asserts reference-patch validates all cases and that
> `control:bad_patch`, `control:malformed_patch`, `control:detects_no_patch` and
> `control:keyword_gamer` validate none.

Control behavior verified by: Hari Kancharla   Date: 2026-04-09

## 11. Final admission decision

Decision (accepted / hold / rejected / deprecated): accepted
Acceptance level (provisional / paper-grade): provisional
Builder: Hari Kancharla   Date: 2026-04-09
Independent reviewer (required for paper-grade; a real person, not the builder
or any automation): __________________  Date: __________
