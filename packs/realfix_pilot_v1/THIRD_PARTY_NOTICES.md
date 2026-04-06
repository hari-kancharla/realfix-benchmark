# Third-party notices - RealFix Pilot v1

This benchmark pack vendors source and test files from third-party open-source
projects so that each case is a complete, runnable reverse-review snapshot. The
redistributed files are reproduced under the upstream licenses in effect at the
pinned commits below. The full upstream license text for each project is included
in `licenses/`. This document preserves the notices accompanying the redistributed
files; it is a redistribution record, not legal advice. No third-party content is
relicensed by this repository.

Each case vendors the selected source tree at the **buggy** commit (as `after/`)
and at the **fixed** commit (as `before/`), and the selected test tree at the fixed
commit (as `tests/`). The exact selectors and changed paths for each case are
recorded in `sources/realfix_pilot_v1/<case-id>/evidence.yaml`.

## more_itertools_windowed_zero_size_001

- Project: more-itertools
- Source repository: https://github.com/more-itertools/more-itertools
- License: MIT
- License files:
  - `licenses/more_itertools-MIT.txt` (`LICENSE`)
- Buggy commit: `e4d2a4a2a97246a73856754b2c4866d7f41d4875`
- Fixed commit: `71b46b06fb48abcd2f7a26d74c148a650d340386`
- Included content: the `more_itertools` source tree (buggy and fixed)
  and the `tests` tree at the fixed commit. Changed source path:
  `more_itertools/more.py`.

## packaging_dependency_group_error_cache_001

- Project: packaging
- Source repository: https://github.com/pypa/packaging
- License: Apache-2.0 OR BSD-2-Clause
- License files:
  - `licenses/packaging-LICENSE.txt` (`LICENSE`)
  - `licenses/packaging-Apache-2.0.txt` (`LICENSE.APACHE`)
  - `licenses/packaging-BSD-2-Clause.txt` (`LICENSE.BSD`)
- Buggy commit: `e64c20eb7a854c72710d4c962bc8a95f343230e6`
- Fixed commit: `349abfad0688f42eb835ed8a10380d6cbf6940e7`
- Included content: the `src/packaging` source tree (buggy and fixed)
  and the `tests` tree at the fixed commit. Changed source path:
  `src/packaging/dependency_groups.py`.

## packaging_direct_url_at_in_password_001

- Project: packaging
- Source repository: https://github.com/pypa/packaging
- License: Apache-2.0 OR BSD-2-Clause
- License files:
  - `licenses/packaging-LICENSE.txt` (`LICENSE`)
  - `licenses/packaging-Apache-2.0.txt` (`LICENSE.APACHE`)
  - `licenses/packaging-BSD-2-Clause.txt` (`LICENSE.BSD`)
- Buggy commit: `28c299e8a823600dd66d4adeb7c7cc98e11089d2`
- Fixed commit: `08bb047794f4e70b157dacef4538b3a6e3492743`
- Included content: the `src/packaging` source tree (buggy and fixed)
  and the `tests` tree at the fixed commit. Changed source path:
  `src/packaging/direct_url.py`.

## packaging_empty_project_name_001

- Project: packaging
- Source repository: https://github.com/pypa/packaging
- License: Apache-2.0 OR BSD-2-Clause
- License files:
  - `licenses/packaging-LICENSE.txt` (`LICENSE`)
  - `licenses/packaging-Apache-2.0.txt` (`LICENSE.APACHE`)
  - `licenses/packaging-BSD-2-Clause.txt` (`LICENSE.BSD`)
- Buggy commit: `fb82782df51f9a33bf9d2a489361a3784bb739ff`
- Fixed commit: `84833cc16be84bc7f1d9f64e2818afe0dd48aade`
- Included content: the `src/packaging` source tree (buggy and fixed)
  and the `tests` tree at the fixed commit. Changed source path:
  `src/packaging/utils.py`.

## packaging_infinity_self_comparison_001

- Project: packaging
- Source repository: https://github.com/pypa/packaging
- License: Apache-2.0 OR BSD-2-Clause
- License files:
  - `licenses/packaging-LICENSE.txt` (`LICENSE`)
  - `licenses/packaging-Apache-2.0.txt` (`LICENSE.APACHE`)
  - `licenses/packaging-BSD-2-Clause.txt` (`LICENSE.BSD`)
- Buggy commit: `4339d3a0028348e21863664e6022e3cff20c3411`
- Fixed commit: `f8f16338e10d5d509ea2a29e0f0cf56baf4be565`
- Included content: the `src/packaging` source tree (buggy and fixed)
  and the `tests` tree at the fixed commit. Changed source path:
  `src/packaging/_structures.py`.

## packaging_nested_extra_normalization_001

- Project: packaging
- Source repository: https://github.com/pypa/packaging
- License: Apache-2.0 OR BSD-2-Clause
- License files:
  - `licenses/packaging-LICENSE.txt` (`LICENSE`)
  - `licenses/packaging-Apache-2.0.txt` (`LICENSE.APACHE`)
  - `licenses/packaging-BSD-2-Clause.txt` (`LICENSE.BSD`)
- Buggy commit: `349abfad0688f42eb835ed8a10380d6cbf6940e7`
- Fixed commit: `07265129295b4b95b9143b50e3ce4709f31a8c49`
- Included content: the `src/packaging` source tree (buggy and fixed)
  and the `tests` tree at the fixed commit. Changed source path:
  `src/packaging/markers.py`.

## packaging_normalized_name_double_hyphen_001

- Project: packaging
- Source repository: https://github.com/pypa/packaging
- License: Apache-2.0 OR BSD-2-Clause
- License files:
  - `licenses/packaging-LICENSE.txt` (`LICENSE`)
  - `licenses/packaging-Apache-2.0.txt` (`LICENSE.APACHE`)
  - `licenses/packaging-BSD-2-Clause.txt` (`LICENSE.BSD`)
- Buggy commit: `283811bffee5da95bda6d5332cb88f8b231187a2`
- Fixed commit: `ba17fcea2367a70cba21d6bfb0931ae476ee8583`
- Included content: the `src/packaging` source tree (buggy and fixed)
  and the `tests` tree at the fixed commit. Changed source path:
  `src/packaging/utils.py`.

The original per-file copyright and SPDX notices present in the upstream
files are retained as-is in the vendored `before/`, `after/`, and `tests/` trees.
