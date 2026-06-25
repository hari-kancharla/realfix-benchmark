# realfix-benchmark

Execution-verified historical code-review benchmark cases for
[Code Review Arena](https://github.com/harihkk/code-review-arena).

This repository is a **separate, versioned dataset** that vendors complete,
runnable reverse-review snapshots derived from real upstream bug fixes. It exists
because each case bundles a full source-plus-tests tree, which does not scale
cleanly inside the core harness repository. The core repository remains the
harness; this repository holds the data.

## RealFix Pilot v1 — Batch 1

This is **RealFix Pilot v1, Batch 1**. It is a small methodology batch, **not** the
complete Pilot v1.

- It contains **2 execution-verified cases** (a third approved candidate, tomlkit,
  could not be built — see below — and is documented as a failed candidate).
- Cases are **synthetic reverse-review cases derived from real fixes**: `after/` is
  the source *before* the historical repair, `before/` is the source *after* it, and
  the synthetic `pr.diff` is the inverse of the real change. They are **not** the
  original bug-introducing pull requests.
- The batch supports **no model-performance conclusions**. It is a methodology
  pilot, not a paper-scale benchmark.
- The full Pilot v1 target remains **at least 12 diverse, verified cases**.

### Built cases (both `verified` via Docker)

| case id | upstream | category | license |
|---|---|---|---|
| `more_itertools_windowed_zero_size_001` | more-itertools/more-itertools | input-validation | MIT |
| `packaging_dependency_group_error_cache_001` | pypa/packaging | state-management | Apache-2.0 OR BSD-2-Clause |

### Held / failed candidates (not built)

- **Rich** `39ee57dfe70614381c3ebce34cb35cab557af2f5` — **HOLD**, reason
  `intermediate_fix_superseded_during_review`: the selected commit is an intermediate
  implementation inside PR #3938 that was followed by further implementation and test
  commits. Not auto-replaced.
- **tomlkit** `d548e18b71b28d0e9628127bf0b9dfc5a254dca0` (PR #527) — **FAILED**, reason
  `tests_tree_contains_submodule`: at the fixed commit the `tests/` tree contains a git
  submodule (`tests/toml-test`, gitlink mode `160000`) that the importer correctly
  refuses to materialize, and the targeted test sits beside it at the `tests/` root, so
  no submodule-free `tests_root` exists. It cannot be imported without weakening
  importer policy, which is out of scope. Evidence is retained under `sources/` as a
  documented failed candidate. Not auto-replaced.

### Selection bias (honest limitation)

Admission favors **clean, hermetic source-plus-test commit ranges**: the importer
requires every changed path to be classifiable as selected source or tests, and the
test must run offline with no plugins or submodules. This systematically excludes
fixes that bundle changelogs/news, use git submodules for test data, or need network
or third-party pytest plugins, and biases the corpus toward small fixes in
zero-dependency libraries. This must be reported in any eventual analysis.

## Protocol and governance

The methodology for building and admitting cases is defined in:

- [`docs/benchmark-protocol-v0.1.md`](docs/benchmark-protocol-v0.1.md) — case
  lifecycle, RealFix case definition, historical-interval, regression, mutation, and
  contamination policies, and stable reason codes.
- [`docs/case-admission-checklist.md`](docs/case-admission-checklist.md) — the
  per-case checklist a human reviewer completes before a case is accepted.
- [`docs/provenance-and-attribution.md`](docs/provenance-and-attribution.md) —
  license retrieval, notice preservation, and attribution policy.
- [`docs/evaluation-plan.md`](docs/evaluation-plan.md) — the planned evaluation,
  provisional research questions, and go/no-go signals for scaling beyond the pilot.

## Layout

```
sources/realfix_pilot_v1/<case-id>/{import-spec.yaml, evidence.yaml}   # human inputs
packs/realfix_pilot_v1/                                                # generated pack
  manifest.yaml  pack.sha256  THIRD_PARTY_NOTICES.md  licenses/  <case dirs>
docker/realfix_pilot/{Dockerfile, requirements.txt, build.sh}         # hermetic test image
scripts/rebuild_batch_01.py                                           # deterministic rebuilder
docs/batch-01-report.md                                               # full results
requirements-harness.txt                                             # pinned Code Review Arena
```

## Reproduce

```bash
pip install -r requirements-harness.txt          # Code Review Arena pinned @ 3e77aa1
docker/realfix_pilot/build.sh                     # build realfix-pilot-batch-01:1
python scripts/rebuild_batch_01.py                # deterministic pack rebuild
arena validate packs/realfix_pilot_v1
arena lint-cases packs/realfix_pilot_v1 --strict
arena certify-pack packs/realfix_pilot_v1 --limit 20 --determinism-runs 3
```

## Licensing

The dataset metadata and automation in this repository will receive an explicit
project license before any public release; it is currently unlicensed-pending.
Vendored upstream source and tests remain under their **upstream** licenses, which
are preserved per pack in `packs/<pack>/licenses/` and recorded in
`packs/<pack>/THIRD_PARTY_NOTICES.md`. No third-party content is relicensed here.
See [`LICENSES/README.md`](LICENSES/README.md).
