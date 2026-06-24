# RealFix Pilot v1 — Batch 1 report

**This is RealFix Pilot v1, Batch 1: a methodology batch, not the complete Pilot v1.**
It contains **2 execution-verified cases** (one approved candidate, tomlkit, could
not be built and is documented as failed). The cases are **synthetic reverse-review
cases derived from real fixes**, not the original bug-introducing pull requests. The
batch supports **no model-performance conclusions**. The full Pilot v1 target remains
**at least 12 diverse, verified cases**.

## Pinned harness

Code Review Arena pinned to merge commit
`3e77aa1a13fde271cce02b4b716dd74add1e547c` (PR #22). The harness is used only as an
external, pinned tool; it is neither vendored nor modified by this repository.

## Docker environment

- Image: `realfix-pilot-batch-01:1` (built from `docker/realfix_pilot/`).
- Base `python:3.11-slim` (Python 3.11.15). Pinned runtime: `pytest==8.3.5` **only**.
- Confirmed: the two built cases need no runtime dependency beyond pytest (no
  hypothesis or other plugin/import). Tests run with `--network none`, no credentials,
  no Docker socket, no submodules, no package installation during a run.

## Cases

### more_itertools_windowed_zero_size_001
- Upstream: more-itertools/more-itertools (MIT)
- Buggy `e4d2a4a2a97246a73856754b2c4866d7f41d4875` → Fixed `71b46b06fb48abcd2f7a26d74c148a650d340386`
- Issue #1057, PR #1139 (author Raymond Hettinger)
- Defect: `windowed()` accepted a window size of zero and yielded one empty tuple
  instead of rejecting the size; only negative sizes were rejected.
- Changed source: `more_itertools/more.py`; tests: `tests/test_more.py`
- Regression: `tests/test_more.py::...::test_invalid_n`
- Test command: `pytest tests/test_more.py -q`
- baseline: fail (exit 1, `ValueError not raised`); reference: pass
- mutation: **100% kill (20 mutants)**; determinism: 3/3 stable → **verified**

### packaging_dependency_group_error_cache_001
- Upstream: pypa/packaging (Apache-2.0 OR BSD-2-Clause)
- Buggy `e64c20eb7a854c72710d4c962bc8a95f343230e6` → Fixed `349abfad0688f42eb835ed8a10380d6cbf6940e7`
- Issue #1239, PR #1248
- Defect: a failed dependency-group parse was stored and replayed on later lookups,
  and a non-string include entry was accepted instead of rejected.
- Changed source: `src/packaging/dependency_groups.py`; tests: `tests/test_dependency_groups.py`
- Regression: `tests/test_dependency_groups.py::test_malformed_group_entries_are_not_cached_on_resolver_instance`
- Test command: `pytest tests/test_dependency_groups.py -q`
- baseline: fail (exit 1); reference: pass
- mutation: **100% kill (7 viable mutants)**; determinism: 3/3 stable → **verified**

## Certification summary

`arena certify-pack packs/realfix_pilot_v1 --limit 20 --determinism-runs 3`
(Docker) → pack level **verified**; both cases **verified**. Neither case has zero
viable mutants; both measured a 100% kill rate at the stated mutant counts.

## Controls (Docker, full mode)

| reviewer | validated repair |
|---|---|
| reference-patch | 2 / 2 |
| control:bad_patch | 0 / 2 |
| control:malformed_patch | 0 / 2 |
| control:detects_no_patch | 0 / 2 |
| control:keyword_gamer | 0 / 2 |

`reference-patch` (apply the gold patch) is the general perfect-patch oracle and
validates 2/2. `control:perfect_patch` is **not** used: it is fixture-bound to the
core repository's bespoke case ids and is not a general oracle for new cases.

## Pack integrity

- `pack.sha256`: `d69c1f50996a53e8f2a47ce0fc74598503d9e08e1d2233d0f928d4036bae7c16`
- Deterministic rebuild: two consecutive runs of `scripts/rebuild_batch_01.py`
  produced byte-identical pack content and an identical checksum.
- License/notice files (`THIRD_PARTY_NOTICES.md`, `licenses/*`) are included in the
  pack and covered by `pack.sha256`.

## Vendored licenses

| project | SPDX | files |
|---|---|---|
| more-itertools | MIT | `licenses/more_itertools-MIT.txt` (blob `0a523bec…`) |
| packaging | Apache-2.0 OR BSD-2-Clause | `licenses/packaging-LICENSE.txt` (`6f62d44e…`), `licenses/packaging-Apache-2.0.txt` (`f433b1a5…`), `licenses/packaging-BSD-2-Clause.txt` (`42ce7b75…`) |

## Held / failed candidates

- **Rich** `39ee57dfe70614381c3ebce34cb35cab557af2f5` — HOLD,
  `intermediate_fix_superseded_during_review` (intermediate commit inside PR #3938,
  followed by further implementation/test commits). Not auto-replaced.
- **tomlkit** `d548e18b71b28d0e9628127bf0b9dfc5a254dca0` (PR #527) — FAILED,
  `tests_tree_contains_submodule`: the `tests/` tree contains the `tests/toml-test`
  git submodule (gitlink mode `160000`), which the importer correctly refuses to
  materialize; the targeted test sits at the `tests/` root beside the gitlink, so no
  submodule-free `tests_root` exists. Importer policy was not weakened. Not
  auto-replaced. Evidence retained under `sources/`.

## Limitations

- Two cases, not three (tomlkit blocked) and not the 12-case Pilot v1.
- Both cases are correctness/validation/state fixes in zero-dependency libraries;
  category and size diversity is narrow.
- Selection bias toward clean, hermetic source-plus-test commit ranges (the importer's
  classifiable-path requirement plus offline/no-plugin/no-submodule execution) excludes
  changelog-bundled, submodule-backed, network- or plugin-dependent fixes. This bias
  must be reported in any eventual analysis.
- Synthetic reverse-review framing and hindsight leakage (the regression test was
  written with the fix) mean difficulty is likely understated relative to live review.
