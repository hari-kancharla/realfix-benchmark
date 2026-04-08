# realfix-benchmark

Execution-verified historical code-review benchmark cases for
[Code Review Arena](https://github.com/hari-kancharla/code-review-arena).

**Code Review Arena is the harness; this repository is its dataset.** Arena is the
product that runs and scores reviewers; RealFix is the execution-verified case data it
runs against. They are split because each case bundles a full source-plus-tests tree,
which does not scale cleanly inside the harness repository. This repository is the
**single authoritative home of every RealFix case** — the harness repository holds no
case data of its own. Arena is consumed here as an external, pinned dependency
(`requirements-harness.txt`); nothing in this repository is vendored into it.

## RealFix Pilot v1

This pack contains **25 cases**: the original Batch 1 pair, 18 Batch 2 additions, and
5 Batch 3 cases consolidated from the harness repository's former `realfix_seed_v0`
seed. Count is past the protocol's "at least 12" methodology target. That does **not**
make the pack ranking-scale. Twenty-five cases still cannot support model-performance
conclusions; a two-proportion detection gap on this size remains coarse. Batch 1 cases
stay `batch-01 accepted`. Batch 2 and Batch 3 cases are **provisional** until this
repository's CI re-certifies them under the current image and a human completes the
admission checklist. Do not treat provisional cases as paper-grade.

The hermetic test image is `realfix-pilot:2`. It supersedes `realfix-pilot-batch-01:1`
and adds the pinned `hypothesis` runtime that some upstream test modules import at
collection time. Because the image changed, CI re-certifies **all 25** cases rather
than carrying prior certification forward.

Every case carries an `origin` block recording its fix's public date and the basis for
that date, which supports the harness's training-data exposure split. The dates are read
from the upstream commit objects by the importer, never entered by hand.

- Cases are **synthetic reverse-review cases derived from real fixes**: `after/` is
  the source *before* the historical repair, `before/` is the source *after* it, and
  the synthetic `pr.diff` is the inverse of the real change. They are **not** the
  original bug-introducing pull requests.
- The windowed more-itertools fix already in Batch 1 was **not** imported again.

### Built cases

| case id | upstream | batch | category | license |
|---|---|---|---|---|
| `more_itertools_windowed_zero_size_001` | more-itertools/more-itertools | 1 accepted | input-validation | MIT |
| `packaging_dependency_group_error_cache_001` | pypa/packaging | 1 accepted | state-management | Apache-2.0 OR BSD-2-Clause |
| `packaging_infinity_self_comparison_001` | pypa/packaging | 2 provisional | correctness | Apache-2.0 OR BSD-2-Clause |
| `packaging_normalized_name_double_hyphen_001` | pypa/packaging | 2 provisional | correctness | Apache-2.0 OR BSD-2-Clause |
| `packaging_direct_url_at_in_password_001` | pypa/packaging | 2 provisional | security | Apache-2.0 OR BSD-2-Clause |
| `packaging_empty_project_name_001` | pypa/packaging | 2 provisional | correctness | Apache-2.0 OR BSD-2-Clause |
| `packaging_nested_extra_normalization_001` | pypa/packaging | 2 provisional | correctness | Apache-2.0 OR BSD-2-Clause |
| `packaging_license_empty_parens_001` | pypa/packaging | 2 provisional | correctness | Apache-2.0 OR BSD-2-Clause |
| `more_itertools_numeric_range_reversed_empty_001` | more-itertools/more-itertools | 2 provisional | correctness | MIT |
| `more_itertools_split_before_empty_001` | more-itertools/more-itertools | 2 provisional | correctness | MIT |
| `more_itertools_last_reversed_none_001` | more-itertools/more-itertools | 2 provisional | correctness | MIT |
| `more_itertools_chunked_even_001` | more-itertools/more-itertools | 2 provisional | correctness | MIT |
| `more_itertools_split_after_maxsplit_001` | more-itertools/more-itertools | 2 provisional | correctness | MIT |
| `idna_invalid_alabel_001` | kjd/idna | 2 provisional | correctness | BSD-3-Clause |
| `idna_non_ascii_bytes_encode_001` | kjd/idna | 2 provisional | correctness | BSD-3-Clause |
| `idna_non_string_input_001` | kjd/idna | 2 provisional | correctness | BSD-3-Clause |
| `idna_unknown_codepoint_joiner_001` | kjd/idna | 2 provisional | correctness | BSD-3-Clause |
| `installer_path_traversal_001` | pypa/installer | 2 provisional | security | MIT |
| `installer_unbound_executable_001` | pypa/installer | 2 provisional | correctness | MIT |
| `tomli_text_mode_load_001` | hukkin/tomli | 2 provisional | correctness | MIT |
| `attrs_frozen_error_message_001` | python-attrs/attrs | 3 provisional | correctness | MIT |
| `click_shared_default_precedence_001` | pallets/click | 3 provisional | correctness | BSD-3-Clause |
| `packaging_marker_extra_normalization_001` | pypa/packaging | 3 provisional | correctness | Apache-2.0 OR BSD-2-Clause |
| `packaging_name_validation_newline_001` | pypa/packaging | 3 provisional | correctness | Apache-2.0 OR BSD-2-Clause |
| `rich_table_padding_width_001` | Textualize/rich | 3 provisional | correctness | MIT |

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
scripts/rebuild_pack.py                                               # deterministic rebuilder
docs/batch-01-report.md                                               # Batch 1 results
docs/batch-02-report.md                                               # Batch 2 (provisional)
docs/batch-03-report.md                                               # Batch 3 (consolidated)
requirements-harness.txt                                             # pinned Code Review Arena
```

## Reproduce

```bash
pip install -r requirements-harness.txt          # Code Review Arena, pinned
docker/realfix_pilot/build.sh                     # build realfix-pilot:2
python scripts/rebuild_pack.py                    # deterministic pack rebuild
arena validate packs/realfix_pilot_v1
arena lint-cases packs/realfix_pilot_v1 --strict
arena certify-pack packs/realfix_pilot_v1 --limit 25 --determinism-runs 3
```

## Licensing

The dataset metadata and automation in this repository will receive an explicit
project license before any public release; it is currently unlicensed-pending.
Vendored upstream source and tests remain under their **upstream** licenses, which
are preserved per pack in `packs/<pack>/licenses/` and recorded in
`packs/<pack>/THIRD_PARTY_NOTICES.md`. No third-party content is relicensed here.
See [`LICENSES/README.md`](LICENSES/README.md).
