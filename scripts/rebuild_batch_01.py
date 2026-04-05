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
DOCKER_IMAGE = "realfix-pilot-batch-01:1"

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
    # tomlkit_malformed_array_element_001 is intentionally excluded from Batch 1:
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
