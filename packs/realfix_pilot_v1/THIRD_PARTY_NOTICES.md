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

## idna_invalid_alabel_001

- Project: idna
- Source repository: https://github.com/kjd/idna
- License: BSD-3-Clause
- License files:
  - `licenses/idna-BSD-3-Clause-2013-2021.txt` (`LICENSE.md`)
- Buggy commit: `c3383c97b3fffd8aa73aaefd16baf9c6da1e9f4e`
- Fixed commit: `4fdcc18d1eb214b35e16c372e8682fb8b8a52e11`
- Included content: the `idna` source tree (buggy and fixed)
  and the `tests` tree at the fixed commit. Changed source path:
  `idna/core.py`.

## idna_non_ascii_bytes_encode_001

- Project: idna
- Source repository: https://github.com/kjd/idna
- License: BSD-3-Clause
- License files:
  - `licenses/idna-BSD-3-Clause-2013-2021.txt` (`LICENSE.md`)
- Buggy commit: `522c0ebe02d8bd09039dd593e7c152ab5a1d26dd`
- Fixed commit: `e00ed2854c5203be201940f4029a747684594409`
- Included content: the `idna` source tree (buggy and fixed)
  and the `tests` tree at the fixed commit. Changed source path:
  `idna/core.py`.

## more_itertools_chunked_even_001

- Project: more-itertools
- Source repository: https://github.com/more-itertools/more-itertools
- License: MIT
- License files:
  - `licenses/more_itertools-MIT.txt` (`LICENSE`)
- Buggy commit: `c0780fbbba9655d36de09b872981ffd4a90eb120`
- Fixed commit: `49a4b3c94b0d71cc4576df3df9ca90197b5ec9fc`
- Included content: the `more_itertools` source tree (buggy and fixed)
  and the `tests` tree at the fixed commit. Changed source path:
  `more_itertools/more.py`.

## more_itertools_last_reversed_none_001

- Project: more-itertools
- Source repository: https://github.com/more-itertools/more-itertools
- License: MIT
- License files:
  - `licenses/more_itertools-MIT.txt` (`LICENSE`)
- Buggy commit: `c834d6e4a0c4280b7b7750cb0de8dd8acb3d4c2c`
- Fixed commit: `cca32949f12d473fd823e37a5530c30d2faa1332`
- Included content: the `more_itertools` source tree (buggy and fixed)
  and the `tests` tree at the fixed commit. Changed source path:
  `more_itertools/more.py`.

## more_itertools_numeric_range_reversed_empty_001

- Project: more-itertools
- Source repository: https://github.com/more-itertools/more-itertools
- License: MIT
- License files:
  - `licenses/more_itertools-MIT.txt` (`LICENSE`)
- Buggy commit: `247e15b3a489d5805375c95dfa79486c9bd0eb1b`
- Fixed commit: `edb3346f835ca917efbfda5e2d6664ab952da369`
- Included content: the `more_itertools` source tree (buggy and fixed)
  and the `tests` tree at the fixed commit. Changed source path:
  `more_itertools/more.py`.

## more_itertools_split_after_maxsplit_001

- Project: more-itertools
- Source repository: https://github.com/more-itertools/more-itertools
- License: MIT
- License files:
  - `licenses/more_itertools-MIT.txt` (`LICENSE`)
- Buggy commit: `6793bd3e4ed15318746ed2511733f12a9932eb64`
- Fixed commit: `9245cd04c043d0d646497934df72549943d5f868`
- Included content: the `more_itertools` source tree (buggy and fixed)
  and the `tests` tree at the fixed commit. Changed source path:
  `more_itertools/more.py`.

## more_itertools_split_before_empty_001

- Project: more-itertools
- Source repository: https://github.com/more-itertools/more-itertools
- License: MIT
- License files:
  - `licenses/more_itertools-MIT.txt` (`LICENSE`)
- Buggy commit: `c7e73ffbf9c7e15969f9ed301d0431770061ab90`
- Fixed commit: `2e81a562fbaccc996c19c069090a53f52ec894fe`
- Included content: the `more_itertools` source tree (buggy and fixed)
  and the `tests` tree at the fixed commit. Changed source path:
  `more_itertools/more.py`.

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

## packaging_license_empty_parens_001

- Project: packaging
- Source repository: https://github.com/pypa/packaging
- License: Apache-2.0 OR BSD-2-Clause
- License files:
  - `licenses/packaging-LICENSE.txt` (`LICENSE`)
  - `licenses/packaging-Apache-2.0.txt` (`LICENSE.APACHE`)
  - `licenses/packaging-BSD-2-Clause.txt` (`LICENSE.BSD`)
- Buggy commit: `f89652be562e2acd45d4def18977fd9057937c38`
- Fixed commit: `2680259b4fa88885962e1b6f1cca9d92a3e605ca`
- Included content: the `src/packaging` source tree (buggy and fixed)
  and the `tests` tree at the fixed commit. Changed source path:
  `src/packaging/licenses/__init__.py`.

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
