# Evaluation plan

This document describes the evaluation RealFix is being built to support. It defines
the questions and the staging, not any result. No model vendors are chosen here and
no numbers are reported.

## Purpose

Code Review Arena can score a reviewer in several ways: by the text of its review, by
whether it detects the seeded defect, by whether a proposed repair makes the case's
tests pass, and by whether that repair survives mutation-strengthened checks. RealFix
exists to study how those layers of evaluation relate to each other on real
historical defects, using cases that are execution-verified rather than synthetic.

## Provisional research questions

These are the questions the benchmark is meant to investigate. They are provisional
and may be refined as the dataset grows.

1. **Detection versus repair.** What is the gap between detecting a defect and
   producing an execution-validated repair for it?
2. **Repair durability.** How often does an apparently successful repair (one that
   passes the case's tests) fail a stronger mutation-based check?
3. **Ranking stability across evaluation modes.** Do reviewer rankings change when
   the same reviews are scored textually, by detection, by test validation, and by
   mutation-strengthened validation?
4. **Effect of case characteristics.** How do context configuration, defect category,
   and change size affect review performance?
5. **Predictiveness of cheaper scores.** How well do textual or judge-based scores
   predict execution-validated outcomes?

## Staging

The first stage is a methodology pilot of roughly twelve cases. Its purpose is to
exercise the full pipeline end to end and to check whether the questions above are
measurable at all, not to produce paper-scale evidence. Twelve cases are too few to
support claims about model performance, and the pilot will not be presented as if
they did.

Scaling beyond the pilot is a deliberate decision, not an automatic next step. The
following signals, observed in the pilot, would justify scaling; their absence would
be a reason to revise the methodology before adding cases:

- **Measurable variance among reviewers.** Reviewers produce distinguishable results
  rather than collapsing to the same score.
- **A nontrivial detection-versus-repair gap.** Detection and execution-validated
  repair come apart often enough to be worth measuring.
- **Stable repeated evaluations.** Re-running the same evaluation yields consistent
  outcomes, so observed differences are signal rather than noise.
- **Category-level discrimination.** Results differ across defect categories in a way
  the cases can resolve.
- **A meaningful difference between test-only and mutation-strengthened outcomes.**
  Mutation strengthening changes conclusions often enough to be worth its cost.

If these signals are weak, the response is to improve case selection, scoring, or the
evaluation protocol before expanding, rather than to add more cases of the same kind.

## Out of scope here

This task defines the plan only. Choosing model vendors, running reviewers, and
reporting any measurements are separate, later activities. Any eventual report must
carry the limitations already recorded for the pilot: the synthetic reverse-review
framing, hindsight leakage from tests written alongside the fix, and the selection
bias toward clean, hermetic source-plus-test commit ranges.
