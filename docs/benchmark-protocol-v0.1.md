# RealFix benchmark protocol v0.1

This document defines how a RealFix case is discovered, validated, and admitted,
and what each lifecycle status means. It is a governance and methodology document,
not a description of results. It describes the process the Batch 1 cases already
went through and fixes that process so later batches are built the same way.

## What a RealFix case is

A RealFix case is a reverse-review exercise derived from a single real historical
bug fix in an open-source project. A candidate qualifies only when all of the
following hold:

- It corresponds to a real historical defect, not a synthesized or hand-authored
  bug.
- The buggy and fixed states are identifiable Git objects (full commit SHAs, with
  the buggy commit an ancestor of the fixed commit).
- The defect is grounded in maintainer evidence: an issue, a pull request, or
  recorded review discussion that treats the behavior as a defect. A commit message
  or PR title on its own is not sufficient evidence.
- A regression test fails on the buggy tree for the intended behavioral reason
  (an assertion about the defect, not a collection, import, environment, or
  dependency error) and the same test passes on the fixed tree.
- The Git interval between the buggy and fixed commits is completely classifiable
  by the importer: every changed path is either selected source or selected tests.
- The case executes offline and deterministically with no network, credentials,
  external services, or submodules, and without third-party pytest plugins beyond
  what the pinned image provides.
- Third-party licensing and provenance are preserved (see
  `provenance-and-attribution.md`).
- Ground truth can be written from evidence without copying reviewer-visible
  vocabulary (see the contamination policy below).
- The case rebuilds deterministically and certifies through the existing Docker
  ladder.

### What RealFix claims, and what it does not

RealFix cases are **synthetic reverse-review instances derived from real fixes**.
The case presents the source *before* the historical repair as the code under
review (`after/`), presents the source *after* the repair as the reference
solution (`before/`), and presents the inverse of the real change as the synthetic
`pr.diff`. A case is therefore **not** necessarily the original bug-introducing
pull request, and should never be described as one.

The redistributed source, tests, and historical repairs are owned by their upstream
authors and remain under their upstream licenses. RealFix's own contribution is the
selection of fixes, their transformation into reverse-review cases, the provenance
and license records, the validation and certification pipeline, and the scoring and
evaluation methodology. Mining open-source fixes and running their regression tests
are standard techniques and are not claimed as novel in themselves.

## Case lifecycle

A case moves through the statuses below. `hold`, `rejected`, and `deprecated` are
reachable from several earlier statuses. Every failure or hold records a stable
reason code (the recognized codes are listed at the end).

### discovered
- Entry: a candidate fix has been identified in a target repository.
- Required evidence: repository, a candidate fixed commit, an approximate date.
- Permitted actions: read the commit and its surrounding history; do not clone or
  run anything beyond inspection.
- Exit: advance to `screened` once the candidate is worth closer review; otherwise
  `rejected`.

### screened
- Entry: the candidate has been read against the basic admission filters.
- Required evidence: a first judgment that the change is a behavioral fix (not
  documentation, formatting, typing, lint, dependency-only, a feature, or a broad
  refactor), that it touches source and tests, and that a real defect plausibly
  exists.
- Permitted actions: inspect the diff, the linked issue/PR, and the test change;
  record the candidate in the screening registry.
- Exit: advance to `evidence_locked` when the historical evidence is strong;
  otherwise `rejected` (e.g. `no_clear_bug_evidence`, `unrelated_changes`,
  `test_only`, `duplicate_semantics`).

### evidence_locked
- Entry: the candidate's immutable identities and historical evidence are pinned.
- Required evidence: full buggy and fixed SHAs; ordered parent lists; ancestry
  proof; object format; buggy and fixed tree SHAs; the issue and PR URLs and their
  relationship to the fixed commit; the exact changed-path set; license identifier
  and license-file blob SHAs at the pinned commits.
- Permitted actions: record `evidence.yaml`; do not yet build the case.
- Exit: advance to `reproduction_confirmed`; or `rejected`/`hold` if evidence is
  insufficient or the selected commit is an intermediate implementation later
  superseded in review (`intermediate_fix_superseded_during_review`).

### reproduction_confirmed
- Entry: the targeted regression test has actually been run on both trees.
- Required evidence: the exact Python and dependency versions, the exact command,
  the buggy exit status with the failing assertion, the fixed pass result, and a
  statement of whether the run needed network, credentials, services, submodules,
  or plugins.
- Permitted actions: run the targeted test in a clean environment; record results
  honestly using the labels confirmed / inconclusive / failed.
- Exit: advance to `importable`; or `rejected` (`baseline_does_not_fail`,
  `reference_does_not_pass`, `missing_regression_test`, `flaky`, `nonhermetic`).

### importable
- Entry: the case has been built with the pinned `arena import-fix`.
- Required evidence: selectors, tests root, the full changed-path classification,
  and confirmation that the importer accepted the interval.
- Permitted actions: import to a candidate pack; run `arena validate` and
  `arena lint-cases --strict`.
- Exit: advance to `certified`; or `rejected` (`importer_rejected`,
  `changed_path_unclassified`, `semantic_change_uncovered`,
  `tests_tree_contains_submodule`, `protected_path`, `repository_history_override`,
  `shallow_repository`, `contamination`).

### certified
- Entry: the case has been certified through Docker.
- Required evidence: baseline failure, reference pass, mutation result (kill rate or
  an explicit zero-viable-mutant statement), and determinism across the configured
  repeated runs, plus the exact test command and image.
- Permitted actions: run `arena certify-pack` with a mutation limit and determinism
  runs; record the measured numbers.
- Exit: advance to `accepted` when the existing certification policy grants the
  required level and the case clears the control checks; otherwise `hold` or
  `rejected` (`mutation_inadequate`, `flaky`).

### accepted
- Entry: the case is part of a built, certified pack and has cleared admission
  review (see `case-admission-checklist.md`).
- Required evidence: a completed admission checklist with independent sign-off and
  the deterministic-rebuild and control results.
- Permitted actions: include the case in a batch pack and report it.
- Exit: `deprecated` if later invalidated; otherwise it remains accepted.

### hold
- Entry: reachable when a candidate is otherwise plausible but a specific, named
  uncertainty prevents acceptance.
- Required evidence: the blocking reason and what would resolve it.
- Permitted actions: none that change the case; the candidate waits.
- Exit: back to the appropriate earlier status when resolved, or `rejected`. A held
  candidate is never silently auto-replaced.

### rejected
- Entry: reachable from any status when the candidate cannot meet the bar.
- Required evidence: a single stable reason code and a one-line justification; no
  copied source contents.
- Permitted actions: record the rejection in the screening registry.
- Exit: terminal unless re-opened with new evidence.

### deprecated
- Entry: a previously accepted case that is later found invalid or unreproducible,
  or whose upstream objects became unavailable.
- Required evidence: what changed and why the case can no longer be trusted.
- Permitted actions: mark the case deprecated and stop using it; do not delete its
  evidence record.
- Exit: terminal.

## Historical interval policy

The interval between the buggy and fixed commits must be a real, recorded interval.

Permitted intervals:
- One clean fixed commit whose parent is the buggy tree, when the full commit-to-
  parent diff is classifiable.
- A clean contiguous commit range inside a reviewed pull request, when every commit
  in the range is part of the recorded history and the combined diff is classifiable.
- A maintainer merge commit, when its full tree difference against the merge base is
  classifiable.

Prohibited:
- Synthetic cherry-picks or any newly constructed commit that did not exist in the
  recorded history.
- Deleting inconvenient upstream paths to make an interval classifiable.
- Manually reconstructing a fix that was never recorded as a single interval.
- Selecting an intermediate implementation that was later superseded during review,
  unless the protocol explicitly labels and justifies that choice.
- Treating a release or version-bump pull request as the repair pull request.
- Changing history in any way merely to satisfy the importer.

Every case must record full SHAs, parent lists, ancestry proof, buggy and fixed
tree SHAs, the issue/PR relationship to the fixed commit, and the exact changed-path
classification.

## Regression policy

Each case is anchored by a targeted regression test that exercises the specific
defect. The test must fail on the buggy tree because of an assertion about the
defective behavior, and pass on the fixed tree. A failure caused by collection,
import, a missing dependency, a timeout, or any environment problem does not count
as a reproduction; the distinction must be recorded explicitly.

Passing only on the fixed tree is necessary but not sufficient: a test that passes
on the fixed tree but does not fail on the buggy tree for the intended reason does
not demonstrate that the case captures the defect, and the candidate is rejected
(`baseline_does_not_fail`).

A broader historical test file or suite may be used as the certification command
instead of a single function, but only when all of the following hold: the broader
suite existed at the selected fixed commit; the benchmark builder invents and
modifies no tests; the additional scope is recorded in the case evidence; the
broader scope introduces no unrelated nondeterminism; and the exact command is
preserved. This option exists because mutation evidence often depends on exercising
the changed code through more of its existing tests, not because narrow tests are
unacceptable.

Optional dependencies, plugins, submodules, services, and network access are handled
conservatively: the certification image pins only the dependencies a case actually
needs, tests run with networking disabled, and a case that requires a submodule, a
network service, credentials, or an unpinned plugin is rejected (`nonhermetic`,
`tests_tree_contains_submodule`, or `dependency_environment_too_large`).

## Mutation policy

Mutation testing measures whether the case's tests can reject plausible wrong
repairs. A viable mutant is a mutant of the reference solution's changed code that
the build process can execute. The kill rate is the fraction of viable mutants the
recorded test command rejects, reported together with the viable-mutant count and
the mutation limit.

When a case has zero viable mutants, that fact is reported explicitly as
"zero viable mutants," never as a kill rate. Zero mutation evidence is not described
as equivalent to any measured kill rate; a zero-mutant case rests only on its
baseline-fails, reference-passes, and determinism verdicts, and that weaker basis is
stated.

The benchmark builder never manufactures mutants and never adds hidden tests to
raise a kill rate. When the test scope is broadened (per the regression policy) and
that broadening changes the mutation result, the change in scope and its effect on
the mutation numbers are documented in the case evidence.

## Contamination policy

Three kinds of information are kept separate:

- Reviewer-visible information: the synthetic `pr.diff`, the `after/` source under
  review, and the test names the reviewer can see.
- Builder-only evidence: the upstream issue and PR discussion, the maintainer
  repair, and the analysis used to write the case. This is not shown to a reviewer.
- Scoring-only ground truth: the `must_mention` terms, concepts, and acceptable-fix
  keywords used to score a review. These must be derivable from the builder evidence
  without leaking into reviewer-visible surfaces.

Before acceptance, ground-truth vocabulary is checked against bug vocabulary in test
names, explanatory comments and docstrings in the reviewed source, wording derived
from the patch, and language taken directly from the issue or PR. Paraphrasing the
defect in scoring fields is acceptable; copying the answer's distinctive terms into
those fields is prohibited.

The absence of a particular keyword does not by itself prove a case is
contamination-free. Each case records a contamination risk of low, medium, or high
with a short justification, in addition to passing the automated strict lint.
Legitimate upstream comments and regression tests are never deleted or rewritten to
make a contamination check pass; if credible, leak-free ground truth cannot be
written, the candidate is rejected (`contamination`).

## Stable reason codes

`no_clear_bug_evidence`, `unrelated_changes`, `test_only`,
`documentation_or_changelog_only`, `duplicate_semantics`, `unsupported_license`,
`missing_regression_test`, `baseline_does_not_fail`, `reference_does_not_pass`,
`flaky`, `nonhermetic`, `dependency_environment_too_large`,
`tests_tree_contains_submodule`, `importer_rejected`, `changed_path_unclassified`,
`semantic_change_uncovered`, `protected_path`, `repository_history_override`,
`shallow_repository`, `contamination`, `mutation_inadequate`,
`intermediate_fix_superseded_during_review`.
