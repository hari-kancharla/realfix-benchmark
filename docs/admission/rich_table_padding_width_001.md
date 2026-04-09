# Admission checklist - rich_table_padding_width_001

Facts in the `>` blocks are derived from the upstream Git objects and from this
repository's CI. The builder has reviewed them and signed the sections below.

**The independent-reviewer line is deliberately unsigned** - the
protocol requires a second real person for that, and no second reviewer has looked at
this case. The case is therefore *provisionally* accepted, not paper-grade.

```
Case id:       rich_table_padding_width_001
Upstream:      Textualize/rich
Buggy commit:  fe55a131c2780fa856464ad04d7d6dc8a1079b72
Fixed commit:  1c5e03eb32020011f5b13174e186c588d09d749c
Builder: Hari Kancharla            Build date: 2026-04-09
```

## 1. Provenance
- [x] Full buggy and fixed SHAs recorded; object format recorded.
- [x] Buggy is an ancestor of fixed (ancestry proof recorded).
- [x] Buggy and fixed tree SHAs recorded.
- [x] Parent lists recorded; interval matches the historical-interval policy.
- [x] Selected commit is not a superseded intermediate (or is labelled and justified).

> Measured: object format `sha1`; buggy tree `08070be2b24ac37b3e39494ca74cf69d76c99a8e`;
> fixed tree `9e243e1651ba7b196b62bb5d17fe6eee9469a862`. Ancestry is re-proved on every rebuild by
> `scripts/rebuild_pack.py` (`git merge-base --is-ancestor`), which CI runs.

Provenance verified by: Hari Kancharla   Date: 2026-04-09

## 2. Historical evidence
- [x] Issue and/or PR URLs recorded, with their relationship to the fixed commit.
- [x] A maintainer-grounded statement establishes the behavior as a defect.
- [x] The defect is not inferred from the commit message or PR title alone.

> Recorded: issue https://github.com/Textualize/rich/issues/3871
> PR https://github.com/Textualize/rich/pull/3935
> Defect evidence: Issue #3871 reports uneven padding between table cells. PR #3935 ("fix for padding width", merged) rewrites Table._get_padding_width to handle collapsed padding and to drop the outer padding of the first and last columns so spacing is consistent.

Historical evidence verified by: Hari Kancharla   Date: 2026-04-09

## 3. Regression reproduction
- [x] Targeted regression test path and function recorded.
- [x] Buggy run fails for the intended behavioral assertion; failing assertion recorded.
- [x] Fixed run passes.
- [x] Exact Python and dependency versions and the exact command recorded.
- [x] Reproduction label recorded.

> Measured: `tests/test_table.py` :: `test_padding_width`.
> CI verdict **VERIFIED** - baseline_fails=pass, reference_passes=pass,
> deterministic=pass across 3 runs.
> Environment: Python 3.11, pytest 8.3.5, network none.

Regression reproduction verified by: Hari Kancharla   Date: 2026-04-09

## 4. Path classification
- [x] Complete diff name-status recorded; every path classified.
- [x] No unclassified generated/doc/config path.
- [x] Selectors and tests root recorded.

> Measured changed paths: `rich/table.py`, `tests/test_columns.py`, `tests/test_table.py`
> Selectors: `rich`; tests root `tests`.

Path classification verified by: Hari Kancharla   Date: 2026-04-09

## 5. Execution environment
- [x] Networking disabled. No credentials, external services, or submodules.
- [x] No third-party pytest plugin beyond the pinned image.
- [x] Every runtime dependency pinned in the image lock and justified.

> Measured: image `realfix-pilot:2`, network `none`, plugins `none`,
> submodules `none`, extra deps: hypothesis 6.140.3 (import-time only).

Execution environment verified by: Hari Kancharla   Date: 2026-04-09

## 6. Task-surface leakage
- [x] Ground-truth vocabulary checked against tests, comments, filenames, patch wording.
- [x] Scoring fields paraphrase rather than copy distinctive terms.
- [x] Strict contamination lint passes.
- [x] Leakage risk recorded low / medium / high with justification.
- [x] No upstream comment or test deleted or rewritten to pass lint.

> Measured: `arena lint-cases --strict` passes on this pack in CI.
> Analysis: Note for the reviewer: the added upstream test is named test_padding_width and the ground-truth concept is "cell padding width". The overlap is upstream's own naming, not introduced here. Strict contamination lint passes.
> Leakage risk: **medium** - an upstream test name echoes a ground-truth concept; the name is upstream's own and was not renamed to pass lint.

Task-surface leakage verified by: Hari Kancharla   Date: 2026-04-09

## 6b. Historical exposure
- [x] Upstream fix date, issue/PR public date, benchmark publication date recorded.
- [x] Exposure risk recorded with justification.
- [x] Collection-vs-model-release relationship recorded.
- [x] Retrieval-during-evaluation recorded.

> Measured: upstream fix date `2026-01-23`, read from the commit object by the
> importer and carried in the case's `origin` block.
> Exposure risk: **low** - the fix became public on 2026-01-23, recently enough that it may postdate the evaluated model's cutoff; this is a date relationship, not proof of non-exposure.

Historical exposure verified by: Hari Kancharla   Date: 2026-04-09

## 7. Mutation
- [x] Mutation run recorded with limit and viable-mutant count.
- [x] Kill rate recorded, or "zero viable mutants" recorded explicitly.
- [x] Zero mutation evidence not presented as a measured kill rate.
- [x] No mutants manufactured, no hidden tests added.

> Measured on `realfix-pilot:2` at limit 25: **84% kill on 25 mutants**.

Mutation verified by: Hari Kancharla   Date: 2026-04-09

## 8. Licensing
- [x] Upstream SPDX and license-file blob SHAs at the pinned commit recorded.
- [x] Exact pinned license texts vendored (all files for dual licences).
- [x] NOTICE / AUTHORS / data-licence requirements checked.
- [x] Per-case third-party notice recorded; nothing relicensed.

> Measured SPDX: `MIT`
  - `LICENSE` blob `4415505566f261c802b671426be529a31f914137`
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
