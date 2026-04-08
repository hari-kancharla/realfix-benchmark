# Evaluation plan

This document describes the evaluation RealFix is being built to support. It defines
the questions and the staging, not any result. No model vendors are chosen here and
no numbers are reported.

## Purpose

Code Review Arena can score a reviewer in several ways: by the text of its review, by
whether it detects the seeded defect, by whether a proposed repair makes the case's
tests pass, and by whether that repair survives mutation-strengthened checks. RealFix
studies execution-verified historical defects presented as synthetic reverse-review
tasks: the underlying defect and its repair are real and historical, while the task a
reviewer sees is a synthetic reverse-review presentation of that fix. A case is not
necessarily the original bug-introducing pull request. The aim is to study how those
layers of evaluation relate to each other on such cases.

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
they did. Batch 2 grew the pack to 20 cases, which meets the count target and still
does not confer ranking power: more cases of the same hermetic, zero-dependency
kind do not by themselves make detection-versus-repair gaps resolvable.

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

## Development and held-out cases

The evaluation uses the development/held-out split defined in the protocol. Development
cases may be used to debug prompts, output parsing, and tool integration; held-out
evaluation cases are not used for prompt tuning or reviewer-specific debugging, and the
split (and any later change to it) is recorded before evaluation. "Held-out" describes
this researcher discipline, not a guarantee that a public case is absent from a model's
training data — that is the separate historical exposure question below.

## Evaluation freeze and statistical plan

Before any pilot model run, freeze and record: the dataset version and checksum; the
evaluated case IDs; the model or API version; the evaluation date; the prompt; the
context configuration; the tool permissions; the temperature and sampling parameters;
the number of repetitions; the timeout and retry rules; the maximum cost or token
budget; and the definitions of success and failure. The frozen configuration is fixed
before results are seen.

Analysis and reporting follow these rules:

- The case is the primary unit of analysis.
- When reviewers are evaluated on the same cases, comparisons are paired.
- Aggregate rates are reported with case-level bootstrap confidence intervals.
- Every percentage is reported with its raw numerator and denominator.
- No stochastic run is selected as "best" after observing results.
- Timeout, refusal, malformed output, no patch, invalid patch, and infrastructure
  failure each have a predefined treatment fixed before the run.
- Detection, proposed repair, applicable repair, test-validated repair, and
  mutation-strengthened repair are reported separately.
- Cost and latency are reported.
- Excluded cases and failed runs are disclosed.

This task does not prescribe a model vendor and reports no statistical results.

## Out of scope here

This task defines the plan only. Choosing model vendors, running reviewers, and
reporting any measurements are separate, later activities. Any eventual report must
carry the limitations already recorded for the pilot: the synthetic reverse-review
framing; hindsight leakage from tests written alongside the fix; the selection bias
toward clean, hermetic source-plus-test commit ranges; and the two contamination
threats reported separately — task-surface leakage and historical exposure risk — with
a fresh post-release temporal subset used wherever practical and the limitation
reported plainly when it is not.
