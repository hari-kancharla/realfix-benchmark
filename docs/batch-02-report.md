# RealFix Pilot v1 — Batch 2 report

**This is RealFix Pilot v1, Batch 2: a methodology expansion, not a ranking-scale
release.** It adds **18** historical-fix cases to the Batch 1 pack (2 cases).
The windowed more-itertools fix already present in Batch 1 was not imported
again. The pack now has **20** cases. Twenty cases still support **no
model-performance conclusions**. Crossing the protocol's "at least 12 diverse
verified cases" count does not by itself produce ranking power; a two-proportion
detection gap on this size remains large (on the order of 0.5).

Batch 2 cases are **provisional**. The builder filled evidence and the pinned
importer accepted each snapshot (validation and strict contamination lint at
import time). Paper-grade admission still needs this repository's Docker
certification on `realfix-pilot-batch-01:1` and an independent human checklist
sign-off. This report does not simulate that sign-off.

## What was added

The 18 cases are historical repairs from packaging (6), more-itertools (5),
idna (4), installer (2), and tomli (1). Each case is a synthetic reverse-review
snapshot derived from a real fix, not the original bug-introducing pull request.
Import used `arena import-fix` from the harness pin in `requirements-harness.txt`
(`3e77aa1`), the same command Batch 1 used.

Prior hermetic certification of these commit pairs (Python 3.11, pytest,
mutation limit 20) measured kill rates from 60% to 100% on the viable-mutant
sets. Those runs used a different image tag than `realfix-pilot-batch-01:1`.
They are recorded in each case's `mutation_prospect` as prior evidence, not as
this pack's official certification.

## Held / failed (unchanged)

- **Rich** `39ee57dfe70614381c3ebce34cb35cab557af2f5` — HOLD,
  `intermediate_fix_superseded_during_review`. Not auto-replaced.
- **tomlkit** `d548e18b71b28d0e9628127bf0b9dfc5a254dca0` — FAILED,
  `tests_tree_contains_submodule`. Not auto-replaced.

## Honest limitations

- Selection still favors clean, hermetic source-plus-test commit ranges in
  zero-dependency libraries.
- Several more-itertools cases run the full `tests/test_more.py` module, which
  is slow; GitHub Actions timeout is raised because of that, not because the
  tests grew in scope.
- idna license text differs across years; the pack vendors each distinct
  LICENSE.md blob rather than overwriting a single file.
- Pack-official Docker certification, controls, and a byte-identical double
  rebuild on the 20-case pack are CI's job at the tip; this report does not
  claim they have already passed on GitHub.
