# Provenance and attribution

This document defines how RealFix records the origin of the third-party material it
redistributes and how it attributes that material. It is a working policy, not legal
advice; questions about actual legal obligations should go to someone qualified to
answer them.

## License retrieval from pinned objects

Every case redistributes source and tests from a specific upstream commit. The
license text recorded for a case is read from the upstream repository at the pinned
fixed commit, using the committed Git object, not from the project's current website
or default branch. For each license file the case records the file path and the Git
blob SHA at the pinned commit, so the exact bytes that were redistributed can be
recovered and checked later. When the license blob is identical at the buggy and
fixed commits, that is recorded; when it differs, both are recorded.

## Copyright and notice preservation

The vendored `before/`, `after/`, and `tests/` trees keep the upstream files exactly
as committed, including their per-file copyright headers and any SPDX identifiers.
These are not stripped, rewritten, or normalized. The pack's `THIRD_PARTY_NOTICES.md`
is a redistribution record that names, for each case, the project, the source
repository, the pinned buggy and fixed commits, the applicable license files, and
the content included. The full upstream license text is vendored under the pack's
`licenses/` directory and is covered by `pack.sha256`.

## Handling specific license families

- **MIT and BSD (2- and 3-clause):** vendor the single upstream license file and
  preserve per-file headers. These licenses require the copyright notice and license
  text to accompany redistributed source, which the per-pack `licenses/` directory
  and the unmodified file headers provide.
- **Apache-2.0:** vendor the `LICENSE` text; additionally check for and preserve any
  upstream `NOTICE` file, which Apache-2.0 requires to be carried with
  redistributions when present. Preserve any per-file license headers.
- **Dual-licensed projects (for example "Apache-2.0 OR BSD-2-Clause"):** record the
  exact SPDX expression and vendor every license file the upstream selection notice
  references. The Batch 1 packaging case vendors all three of its license files for
  this reason. RealFix does not pick one side of a dual license on the upstream's
  behalf; it preserves the upstream's own offer.

## Additional upstream artifacts to check

Before accepting a case, check whether the upstream repository carries any of the
following at the pinned commit, and preserve or account for them:

- a top-level `NOTICE` file (especially under Apache-2.0);
- an `AUTHORS` or `CONTRIBUTORS` file referenced by the license;
- separate licenses on test data or fixtures vendored into the case;
- separately licensed or generated content within the selected trees.

If a selected tree contains material under terms incompatible with redistribution in
this benchmark, the case is rejected (`unsupported_license`) rather than stripped.

## No relicensing

RealFix does not relicense third-party code. Vendored upstream source and tests
remain under their upstream licenses. The benchmark's own original material (import
specifications, evidence documents, automation, and documentation) is MIT licensed.
The two license regimes are kept distinct and are never merged into a single blanket
statement.

## Attribution in papers and artifacts

Legal permission to redistribute and academic attribution are different obligations,
and both apply. Beyond satisfying each upstream license, any paper or released
artifact that uses these cases should:

- name the upstream projects whose fixes are used and link their repositories;
- make clear that the cases are synthetic reverse-review instances derived from real
  fixes, and are not the original bug-introducing pull requests;
- credit the upstream authors with the source, tests, and historical repairs, and
  describe RealFix's own contribution as the selection, transformation, provenance,
  validation, scoring, and evaluation methodology;
- avoid implying that mining fixes or running regression tests is itself a novel
  contribution.

Where a project requests a specific citation or acknowledgement form, follow it in
addition to, not instead of, the license requirements.
