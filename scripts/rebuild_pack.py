#!/usr/bin/env python3
"""Deterministically rebuild the RealFix Pilot v1 pack.

This script orchestrates the *pinned* Code Review Arena harness; it does not
reimplement importer or checksum internals. For each case it clones the upstream
repository into a temporary directory, verifies the pinned object identities and
ancestry, calls `arena import-fix` (the merged production command), and assembles
the listed case directories into one pack together with the vendored upstream
license texts and a third-party notice document. It then writes and the caller can
verify `pack.sha256`. All temporary directories are removed on success and failure.

Two consecutive runs produce byte-identical pack content.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

from arena.benchmark.pack_hash import write_checksum

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCES = REPO_ROOT / "sources" / "realfix_pilot_v1"
PACK = REPO_ROOT / "packs" / "realfix_pilot_v1"
PACK_NAME = "RealFix Pilot v1"
PACK_VERSION = "realfix_pilot_v1"
DOCKER_IMAGE = "realfix-pilot:2"

# Pinned, immutable per-case facts. Buggy is the parent of fixed (verified below).
CASES = [
    {
        "id": "more_itertools_windowed_zero_size_001",
        "repo_url": "https://github.com/more-itertools/more-itertools",
        "source_label": "more-itertools/more-itertools",
        "buggy": "e4d2a4a2a97246a73856754b2c4866d7f41d4875",
        "fixed": "71b46b06fb48abcd2f7a26d74c148a650d340386",
        "source_tree": "more_itertools",
        "changed_source": "more_itertools/more.py",
        "project": "more-itertools",
        "spdx": "MIT",
        "licenses": [("LICENSE", "more_itertools-MIT.txt")],
    },
    {
        "id": "packaging_dependency_group_error_cache_001",
        "repo_url": "https://github.com/pypa/packaging",
        "source_label": "pypa/packaging",
        "buggy": "e64c20eb7a854c72710d4c962bc8a95f343230e6",
        "fixed": "349abfad0688f42eb835ed8a10380d6cbf6940e7",
        "source_tree": "src/packaging",
        "changed_source": "src/packaging/dependency_groups.py",
        "project": "packaging",
        "spdx": "Apache-2.0 OR BSD-2-Clause",
        "licenses": [
            ("LICENSE", "packaging-LICENSE.txt"),
            ("LICENSE.APACHE", "packaging-Apache-2.0.txt"),
            ("LICENSE.BSD", "packaging-BSD-2-Clause.txt"),
        ],
    },
    {
        "id": "packaging_infinity_self_comparison_001",
        "repo_url": "https://github.com/pypa/packaging",
        "source_label": "pypa/packaging",
        "buggy": "4339d3a0028348e21863664e6022e3cff20c3411",
        "fixed": "f8f16338e10d5d509ea2a29e0f0cf56baf4be565",
        "source_tree": "src/packaging",
        "changed_source": "src/packaging/_structures.py",
        "project": "packaging",
        "spdx": "Apache-2.0 OR BSD-2-Clause",
        "licenses": [
            ("LICENSE", "packaging-LICENSE.txt"),
            ("LICENSE.APACHE", "packaging-Apache-2.0.txt"),
            ("LICENSE.BSD", "packaging-BSD-2-Clause.txt"),
        ],
    },
    {
        "id": "packaging_normalized_name_double_hyphen_001",
        "repo_url": "https://github.com/pypa/packaging",
        "source_label": "pypa/packaging",
        "buggy": "283811bffee5da95bda6d5332cb88f8b231187a2",
        "fixed": "ba17fcea2367a70cba21d6bfb0931ae476ee8583",
        "source_tree": "src/packaging",
        "changed_source": "src/packaging/utils.py",
        "project": "packaging",
        "spdx": "Apache-2.0 OR BSD-2-Clause",
        "licenses": [
            ("LICENSE", "packaging-LICENSE.txt"),
            ("LICENSE.APACHE", "packaging-Apache-2.0.txt"),
            ("LICENSE.BSD", "packaging-BSD-2-Clause.txt"),
        ],
    },
    {
        "id": "packaging_direct_url_at_in_password_001",
        "repo_url": "https://github.com/pypa/packaging",
        "source_label": "pypa/packaging",
        "buggy": "28c299e8a823600dd66d4adeb7c7cc98e11089d2",
        "fixed": "08bb047794f4e70b157dacef4538b3a6e3492743",
        "source_tree": "src/packaging",
        "changed_source": "src/packaging/direct_url.py",
        "project": "packaging",
        "spdx": "Apache-2.0 OR BSD-2-Clause",
        "licenses": [
            ("LICENSE", "packaging-LICENSE.txt"),
            ("LICENSE.APACHE", "packaging-Apache-2.0.txt"),
            ("LICENSE.BSD", "packaging-BSD-2-Clause.txt"),
        ],
    },
    {
        "id": "packaging_empty_project_name_001",
        "repo_url": "https://github.com/pypa/packaging",
        "source_label": "pypa/packaging",
        "buggy": "fb82782df51f9a33bf9d2a489361a3784bb739ff",
        "fixed": "84833cc16be84bc7f1d9f64e2818afe0dd48aade",
        "source_tree": "src/packaging",
        "changed_source": "src/packaging/utils.py",
        "project": "packaging",
        "spdx": "Apache-2.0 OR BSD-2-Clause",
        "licenses": [
            ("LICENSE", "packaging-LICENSE.txt"),
            ("LICENSE.APACHE", "packaging-Apache-2.0.txt"),
            ("LICENSE.BSD", "packaging-BSD-2-Clause.txt"),
        ],
    },
    {
        "id": "packaging_nested_extra_normalization_001",
        "repo_url": "https://github.com/pypa/packaging",
        "source_label": "pypa/packaging",
        "buggy": "349abfad0688f42eb835ed8a10380d6cbf6940e7",
        "fixed": "07265129295b4b95b9143b50e3ce4709f31a8c49",
        "source_tree": "src/packaging",
        "changed_source": "src/packaging/markers.py",
        "project": "packaging",
        "spdx": "Apache-2.0 OR BSD-2-Clause",
        "licenses": [
            ("LICENSE", "packaging-LICENSE.txt"),
            ("LICENSE.APACHE", "packaging-Apache-2.0.txt"),
            ("LICENSE.BSD", "packaging-BSD-2-Clause.txt"),
        ],
    },
    {
        "id": "packaging_license_empty_parens_001",
        "repo_url": "https://github.com/pypa/packaging",
        "source_label": "pypa/packaging",
        "buggy": "f89652be562e2acd45d4def18977fd9057937c38",
        "fixed": "2680259b4fa88885962e1b6f1cca9d92a3e605ca",
        "source_tree": "src/packaging",
        "changed_source": "src/packaging/licenses/__init__.py",
        "project": "packaging",
        "spdx": "Apache-2.0 OR BSD-2-Clause",
        "licenses": [
            ("LICENSE", "packaging-LICENSE.txt"),
            ("LICENSE.APACHE", "packaging-Apache-2.0.txt"),
            ("LICENSE.BSD", "packaging-BSD-2-Clause.txt"),
        ],
    },
    {
        "id": "more_itertools_numeric_range_reversed_empty_001",
        "repo_url": "https://github.com/more-itertools/more-itertools",
        "source_label": "more-itertools/more-itertools",
        "buggy": "247e15b3a489d5805375c95dfa79486c9bd0eb1b",
        "fixed": "edb3346f835ca917efbfda5e2d6664ab952da369",
        "source_tree": "more_itertools",
        "changed_source": "more_itertools/more.py",
        "project": "more-itertools",
        "spdx": "MIT",
        "licenses": [("LICENSE", "more_itertools-MIT.txt")],
    },
    {
        "id": "more_itertools_split_before_empty_001",
        "repo_url": "https://github.com/more-itertools/more-itertools",
        "source_label": "more-itertools/more-itertools",
        "buggy": "c7e73ffbf9c7e15969f9ed301d0431770061ab90",
        "fixed": "2e81a562fbaccc996c19c069090a53f52ec894fe",
        "source_tree": "more_itertools",
        "changed_source": "more_itertools/more.py",
        "project": "more-itertools",
        "spdx": "MIT",
        "licenses": [("LICENSE", "more_itertools-MIT.txt")],
    },
    {
        "id": "more_itertools_last_reversed_none_001",
        "repo_url": "https://github.com/more-itertools/more-itertools",
        "source_label": "more-itertools/more-itertools",
        "buggy": "c834d6e4a0c4280b7b7750cb0de8dd8acb3d4c2c",
        "fixed": "cca32949f12d473fd823e37a5530c30d2faa1332",
        "source_tree": "more_itertools",
        "changed_source": "more_itertools/more.py",
        "project": "more-itertools",
        "spdx": "MIT",
        "licenses": [("LICENSE", "more_itertools-MIT.txt")],
    },
    {
        "id": "more_itertools_chunked_even_001",
        "repo_url": "https://github.com/more-itertools/more-itertools",
        "source_label": "more-itertools/more-itertools",
        "buggy": "c0780fbbba9655d36de09b872981ffd4a90eb120",
        "fixed": "49a4b3c94b0d71cc4576df3df9ca90197b5ec9fc",
        "source_tree": "more_itertools",
        "changed_source": "more_itertools/more.py",
        "project": "more-itertools",
        "spdx": "MIT",
        "licenses": [("LICENSE", "more_itertools-MIT.txt")],
    },
    {
        "id": "more_itertools_split_after_maxsplit_001",
        "repo_url": "https://github.com/more-itertools/more-itertools",
        "source_label": "more-itertools/more-itertools",
        "buggy": "6793bd3e4ed15318746ed2511733f12a9932eb64",
        "fixed": "9245cd04c043d0d646497934df72549943d5f868",
        "source_tree": "more_itertools",
        "changed_source": "more_itertools/more.py",
        "project": "more-itertools",
        "spdx": "MIT",
        "licenses": [("LICENSE", "more_itertools-MIT.txt")],
    },
    {
        "id": "idna_invalid_alabel_001",
        "repo_url": "https://github.com/kjd/idna",
        "source_label": "kjd/idna",
        "buggy": "c3383c97b3fffd8aa73aaefd16baf9c6da1e9f4e",
        "fixed": "4fdcc18d1eb214b35e16c372e8682fb8b8a52e11",
        "source_tree": "idna",
        "changed_source": "idna/core.py",
        "project": "idna",
        "spdx": "BSD-3-Clause",
        "licenses": [("LICENSE.md", "idna-BSD-3-Clause-2013-2021.txt")],
    },
    {
        "id": "idna_non_ascii_bytes_encode_001",
        "repo_url": "https://github.com/kjd/idna",
        "source_label": "kjd/idna",
        "buggy": "522c0ebe02d8bd09039dd593e7c152ab5a1d26dd",
        "fixed": "e00ed2854c5203be201940f4029a747684594409",
        "source_tree": "idna",
        "changed_source": "idna/core.py",
        "project": "idna",
        "spdx": "BSD-3-Clause",
        "licenses": [("LICENSE.md", "idna-BSD-3-Clause-2013-2021.txt")],
    },
    {
        "id": "idna_non_string_input_001",
        "repo_url": "https://github.com/kjd/idna",
        "source_label": "kjd/idna",
        "buggy": "7e6df7196e6396b5b84b9530eab8272b5ad51898",
        "fixed": "0f4a28d88f8cce54269f0b6a42edf5e6a5424319",
        "source_tree": "idna",
        "changed_source": "idna/core.py",
        "project": "idna",
        "spdx": "BSD-3-Clause",
        "licenses": [("LICENSE.md", "idna-BSD-3-Clause-2013-2026.txt")],
    },
    {
        "id": "idna_unknown_codepoint_joiner_001",
        "repo_url": "https://github.com/kjd/idna",
        "source_label": "kjd/idna",
        "buggy": "1d365e17e10d72d0b7876316fc7b9ca0eebdd38d",
        "fixed": "b0d8f3c45d83b8b9bce0975a59f0c8ab6645694c",
        "source_tree": "idna",
        "changed_source": "idna/core.py",
        "project": "idna",
        "spdx": "BSD-3-Clause",
        "licenses": [("LICENSE.md", "idna-BSD-3-Clause-2013-2024.txt")],
    },
    {
        "id": "installer_path_traversal_001",
        "repo_url": "https://github.com/pypa/installer",
        "source_label": "pypa/installer",
        "buggy": "504fa8f980641c82868af834f5d30b485ad8a902",
        "fixed": "2eccd66b344de24ee7acc6fc01741a8aa2713f05",
        "source_tree": "src/installer",
        "changed_source": "src/installer/destinations.py",
        "project": "installer",
        "spdx": "MIT",
        "licenses": [("LICENSE", "installer-MIT.txt")],
    },
    {
        "id": "installer_unbound_executable_001",
        "repo_url": "https://github.com/pypa/installer",
        "source_label": "pypa/installer",
        "buggy": "de073ce0d45b9249e2b008df5ac391245e89a283",
        "fixed": "6c3118d04e9a279f8f5b972ba797387451c7a6b4",
        "source_tree": "src/installer",
        "changed_source": "src/installer/_core.py",
        "project": "installer",
        "spdx": "MIT",
        "licenses": [("LICENSE", "installer-MIT.txt")],
    },
    {
        "id": "tomli_text_mode_load_001",
        "repo_url": "https://github.com/hukkin/tomli",
        "source_label": "hukkin/tomli",
        "buggy": "e4da05c35a41a4d53fce7af292b94506b1ea68a7",
        "fixed": "8b962e13490a569d4aab90076451def23ed6c6d8",
        "source_tree": "src/tomli",
        "changed_source": "src/tomli/_parser.py",
        "project": "tomli",
        "spdx": "MIT",
        "licenses": [("LICENSE", "tomli-MIT.txt")],
    },
    {
        "id": "attrs_frozen_error_message_001",
        "repo_url": "https://github.com/python-attrs/attrs",
        "source_label": "python-attrs/attrs",
        "buggy": "eccd966d80aff5196efc959316961cfa780439f9",
        "fixed": "ce89f5d11feb0805da9ed10bb165238cc959f1bb",
        "source_tree": "src/attr",
        "changed_source": "src/attr/exceptions.py",
        "project": "attrs",
        "spdx": "MIT",
        "licenses": [("LICENSE", "attrs-MIT.txt")],
    },
    {
        "id": "click_shared_default_precedence_001",
        "repo_url": "https://github.com/pallets/click",
        "source_label": "pallets/click",
        "buggy": "6a1c0d077311f180b356965914e2de5b9e0fdb44",
        "fixed": "1c20dc6e724cd5625faaa17b715ba928d44c08bf",
        "source_tree": "src/click",
        "changed_source": "src/click/core.py",
        "project": "click",
        "spdx": "BSD-3-Clause",
        "licenses": [("LICENSE.txt", "click-BSD-3-Clause.txt")],
    },
    {
        "id": "packaging_marker_extra_normalization_001",
        "repo_url": "https://github.com/pypa/packaging",
        "source_label": "pypa/packaging",
        "buggy": "8a805e3baac2d71958ec0d0beffbe4d51fd5795f",
        "fixed": "1c09ddf30b79428c21aec180f52e10f6dedc1d8a",
        "source_tree": "src/packaging",
        "changed_source": "src/packaging/markers.py",
        "project": "packaging",
        "spdx": "Apache-2.0 OR BSD-2-Clause",
        "licenses": [
            ("LICENSE", "packaging-LICENSE.txt"),
            ("LICENSE.APACHE", "packaging-Apache-2.0.txt"),
            ("LICENSE.BSD", "packaging-BSD-2-Clause.txt"),
        ],
    },
    {
        "id": "packaging_name_validation_newline_001",
        "repo_url": "https://github.com/pypa/packaging",
        "source_label": "pypa/packaging",
        "buggy": "033854a05229074ddb191d67da1f8e0165e665da",
        "fixed": "258202ed7f796bdb8a65252a66c3fbd3e69e97f6",
        "source_tree": "src/packaging",
        "changed_source": "src/packaging/utils.py",
        "project": "packaging",
        "spdx": "Apache-2.0 OR BSD-2-Clause",
        "licenses": [
            ("LICENSE", "packaging-LICENSE.txt"),
            ("LICENSE.APACHE", "packaging-Apache-2.0.txt"),
            ("LICENSE.BSD", "packaging-BSD-2-Clause.txt"),
        ],
    },
    {
        "id": "rich_table_padding_width_001",
        "repo_url": "https://github.com/Textualize/rich",
        "source_label": "Textualize/rich",
        "buggy": "fe55a131c2780fa856464ad04d7d6dc8a1079b72",
        "fixed": "1c5e03eb32020011f5b13174e186c588d09d749c",
        "source_tree": "rich",
        "changed_source": "rich/table.py",
        "project": "rich",
        "spdx": "MIT",
        "licenses": [("LICENSE", "rich-MIT.txt")],
    },
    # tomlkit_malformed_array_element_001 is intentionally excluded from the pack:
    # at the fixed commit the tests/ tree contains a git submodule (tests/toml-test,
    # gitlink mode 160000) that the importer correctly refuses to materialize, and the
    # targeted test sits beside it at the tests/ root, so no submodule-free tests_root
    # exists. It cannot be imported without weakening importer policy. The evidence is
    # retained under sources/ as a documented failed candidate. Not auto-replaced.
]


def _git(args: list[str], cwd: Path) -> str:
    return subprocess.run(
        ["git", "-C", str(cwd), *args], check=True, capture_output=True, text=True
    ).stdout


def _git_bytes(args: list[str], cwd: Path) -> bytes:
    return subprocess.run(
        ["git", "-C", str(cwd), *args], check=True, capture_output=True
    ).stdout


def _verify(clone: Path, case: dict) -> None:
    fmt = _git(["rev-parse", "--show-object-format"], clone).strip()
    if fmt != "sha1":
        raise SystemExit(f"{case['id']}: unexpected object format {fmt}")
    for which in ("buggy", "fixed"):
        kind = _git(["cat-file", "-t", case[which]], clone).strip()
        if kind != "commit":
            raise SystemExit(f"{case['id']}: {which} {case[which]} is {kind}, not commit")
    rc = subprocess.run(
        ["git", "-C", str(clone), "merge-base", "--is-ancestor", case["buggy"], case["fixed"]]
    ).returncode
    if rc != 0:
        raise SystemExit(f"{case['id']}: buggy is not an ancestor of fixed")


_NOTICE_HEADER = """\
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
"""


def _notice_section(case: dict) -> str:
    lic_lines = "\n".join(f"  - `licenses/{dest}` (`{repo}`)" for repo, dest in case["licenses"])
    return (
        f"\n## {case['id']}\n\n"
        f"- Project: {case['project']}\n"
        f"- Source repository: {case['repo_url']}\n"
        f"- License: {case['spdx']}\n"
        f"- License files:\n{lic_lines}\n"
        f"- Buggy commit: `{case['buggy']}`\n"
        f"- Fixed commit: `{case['fixed']}`\n"
        f"- Included content: the `{case['source_tree']}` source tree (buggy and fixed)\n"
        f"  and the `tests` tree at the fixed commit. Changed source path:\n"
        f"  `{case['changed_source']}`.\n"
    )


def main() -> None:
    tmp = Path(tempfile.mkdtemp(prefix="realfix-rebuild-"))
    try:
        if PACK.exists():
            shutil.rmtree(PACK)
        PACK.mkdir(parents=True)
        (PACK / "licenses").mkdir()
        ordered = sorted(CASES, key=lambda c: c["id"])
        notices = _NOTICE_HEADER
        for case in ordered:
            clone = tmp / f"clone-{case['id']}"
            subprocess.run(
                ["git", "clone", "--quiet", case["repo_url"], str(clone)], check=True
            )
            _verify(clone, case)
            out = tmp / f"out-{case['id']}"
            subprocess.run(
                [
                    "arena", "import-fix",
                    "--repo", str(clone),
                    "--buggy-commit", case["buggy"],
                    "--fixed-commit", case["fixed"],
                    "--spec", str(SOURCES / case["id"] / "import-spec.yaml"),
                    "--output", str(out),
                    "--source-label", case["source_label"],
                ],
                check=True,
            )
            shutil.copytree(out / case["id"], PACK / case["id"])
            for repo_path, dest in case["licenses"]:
                blob = _git_bytes(["show", f"{case['fixed']}:{repo_path}"], clone)
                (PACK / "licenses" / dest).write_bytes(blob)
            notices += _notice_section(case)
        notices += (
            "\nThe original per-file copyright and SPDX notices present in the upstream\n"
            "files are retained as-is in the vendored `before/`, `after/`, and `tests/` trees.\n"
        )
        manifest = {
            "version": PACK_VERSION,
            "name": PACK_NAME,
            "default_docker_image": DOCKER_IMAGE,
            "cases": [c["id"] for c in ordered],
        }
        (PACK / "manifest.yaml").write_text(
            yaml.safe_dump(manifest, sort_keys=True, default_flow_style=False), encoding="utf-8"
        )
        (PACK / "THIRD_PARTY_NOTICES.md").write_text(notices, encoding="utf-8")
        checksum = write_checksum(PACK)
        print(f"pack.sha256: {checksum}")
        print(f"cases: {len(ordered)}")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
