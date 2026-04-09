# realfix-benchmark

Real bug fixes from real Python projects, turned into code-review test cases that
actually run.

## What this is

[Code Review Arena](https://github.com/hari-kancharla/code-review-arena) is the tool.
This repository is the data it runs on.

Every RealFix case lives here, and nowhere else. The Arena repository holds the code
that runs and scores reviewers, but it ships no cases. This repository installs Arena
as a pinned dependency and uses it to build and check the cases.

They are separate repositories because each case ships a full copy of a project's
source and tests. That is a lot of data to keep next to the tool.

## How a case works

Each case starts from a real bug fix in a real project. We take the code from just
before the fix and just after it, then show the change backwards. The reviewer sees a
diff that puts the bug back in, and has to catch it.

Inside a case directory:

- `before/` is the fixed code
- `after/` is the buggy code
- `pr.diff` is the real fix, reversed
- `tests/` is the project's own test suite at the fixed commit

These are not the original pull requests that introduced the bugs. We build them from
the fixes. The tests are the upstream project's, unmodified, so a case passes or fails
on real behaviour rather than on our opinion.

Each case also records when its fix became public, read from the upstream commit
itself. Arena uses those dates to check whether a model could have seen the answer
during training.

## What is in the pack

RealFix Pilot v1 holds **25 cases**, added in three batches:

| batch | cases | status |
|---|---:|---|
| 1 | 2 | accepted |
| 2 | 18 | provisional |
| 3 | 5 | provisional |

Provisional means CI has certified the case, but a person has not yet signed off on
the [admission checklist](docs/case-admission-checklist.md). Do not cite provisional
cases as finished results.

**25 cases is too few to rank models.** This is a pilot that proves the method works
end to end. It is not a leaderboard, and the numbers it produces cannot separate one
reviewer from another with any confidence.

Tests run in a pinned Docker image, `realfix-pilot:2`, which contains only pytest and
hypothesis. Cases run offline with no network.

### Cases

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

### Candidates we could not build

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

### What this corpus is biased toward

A case is only admitted if every changed file is clearly either source or test, and
if the test runs offline with no plugins and no submodules. That rules out fixes that
touch changelogs, that keep test data in a submodule, or that need the network.

The result leans toward small fixes in small, dependency-free libraries. Any analysis
built on this pack has to say so.

## Reproduce it

```bash
pip install -r requirements-harness.txt          # Code Review Arena, pinned by commit
docker/realfix_pilot/build.sh                    # build realfix-pilot:2
python scripts/rebuild_pack.py                   # rebuild every case from upstream
arena validate packs/realfix_pilot_v1
arena lint-cases packs/realfix_pilot_v1 --strict
arena certify-pack packs/realfix_pilot_v1 --limit 25 --determinism-runs 3
```

`rebuild_pack.py` clones each upstream project and rebuilds all 25 cases from their
pinned commits. The result is byte-for-byte identical to what is committed here, and
CI checks that on every push. Nothing in this repository is hand-edited into place.

## Layout

```
sources/    the human inputs for each case: what to import, and the evidence for it
packs/      the generated pack: cases, licenses, notices, manifest, checksum
docker/     the pinned test image
scripts/    the rebuilder
docs/       protocol, admission checklist, batch reports, evaluation plan
```

## Documentation

- [Benchmark protocol](docs/benchmark-protocol-v0.1.md) - how a case is defined,
  built, and admitted, and what each rejection reason means
- [Admission checklist](docs/case-admission-checklist.md) - what a person checks
  before a case is accepted
- [Provenance and attribution](docs/provenance-and-attribution.md) - how upstream
  licenses and notices are preserved
- [Evaluation plan](docs/evaluation-plan.md) - what we intend to measure, and what
  would tell us to stop
- Batch reports: [1](docs/batch-01-report.md), [2](docs/batch-02-report.md),
  [3](docs/batch-03-report.md)

## License

The code and case metadata in this repository are MIT licensed. See [LICENSE](LICENSE).

Vendored upstream source and tests keep **their own** upstream licenses. Nothing here
is relicensed. Each pack carries the full license texts in `packs/<pack>/licenses/`
and records what came from where in `packs/<pack>/THIRD_PARTY_NOTICES.md`. See
[`LICENSES/README.md`](LICENSES/README.md) for the details.
