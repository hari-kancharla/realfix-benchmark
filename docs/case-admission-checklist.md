# RealFix case admission checklist

Complete one copy of this checklist for every candidate before it is marked
`accepted`. It is filled in by a human reviewer against the case's `evidence.yaml`,
the built pack, and the certification and control output. Do not auto-fill it and do
not simulate sign-off; an unchecked or unsigned section means that area has not been
reviewed.

Each section has a sign-off line. The reviewer who verifies a section initials and
dates it.

The builder can complete every section for **provisional acceptance** (usable for
internal methodology and pipeline testing, not as paper-grade evidence).
**Paper-grade acceptance** additionally requires an independent second reviewer — a
real person other than the builder — to sign the provenance, historical evidence,
regression reproduction, task-surface leakage, historical exposure, and licensing
sections. Automation or any language model does not count as the independent
reviewer. When no independent human reviewer is available, the case stays
provisionally accepted. Do not simulate sign-off; an unchecked or unsigned section
means that area has not been reviewed.

```
Case id: ______________________________________________
Upstream: _____________________________________________
Buggy commit:  ________________________________________
Fixed commit:  ________________________________________
Builder: ______________________   Build date: _________
```

## 1. Provenance
- [ ] Full buggy and fixed SHAs recorded; object format recorded.
- [ ] Buggy is an ancestor of fixed (ancestry proof recorded).
- [ ] Buggy and fixed tree SHAs recorded.
- [ ] Parent lists recorded; the interval matches the historical-interval policy.
- [ ] The selected commit is not an intermediate implementation later superseded in
      review (or, if it is, the choice is explicitly labelled and justified).

Provenance verified by: __________________  Date: __________

## 2. Historical evidence
- [ ] Issue and/or PR URLs recorded, with their relationship to the fixed commit.
- [ ] A maintainer-grounded statement establishes the behavior as a defect.
- [ ] The defect is not inferred from the commit message or PR title alone.

Historical evidence verified by: __________________  Date: __________

## 3. Regression reproduction
- [ ] Targeted regression test path and function recorded.
- [ ] Buggy run fails for the intended behavioral assertion (not collection/import/
      dependency/timeout/environment); failing assertion recorded.
- [ ] Fixed run passes.
- [ ] Exact Python and dependency versions and the exact command recorded.
- [ ] Reproduction label recorded (confirmed / inconclusive / failed).
- [ ] If a broader historical suite is used, the added scope is recorded and the
      builder invented or modified no tests.

Regression reproduction verified by: __________________  Date: __________

## 4. Path classification
- [ ] Complete `git diff --name-status` between buggy and fixed recorded.
- [ ] Every changed path classified as selected source or selected tests.
- [ ] No unsupported, generated, documentation/changelog, or configuration path is
      left unclassified.
- [ ] Selectors and tests root recorded.

Path classification verified by: __________________  Date: __________

## 5. Execution environment
- [ ] Runs with networking disabled.
- [ ] No credentials, external services, or submodules required.
- [ ] No third-party pytest plugin required beyond the pinned image.
- [ ] Every added runtime dependency is pinned in the image lock and justified.

Execution environment verified by: __________________  Date: __________

## 6. Task-surface leakage
- [ ] Ground-truth vocabulary checked against test names and bodies,
      comments/docstrings, file names, patch-derived wording, and issue/PR language.
- [ ] Scoring fields paraphrase the defect rather than copying its distinctive terms.
- [ ] Strict contamination lint passes.
- [ ] Task-surface leakage risk recorded as low / medium / high with justification.
- [ ] No upstream comment or regression test was deleted or rewritten to pass lint.

Task-surface leakage verified by: __________________  Date: __________

## 6b. Historical exposure
- [ ] Upstream fix date, issue/PR public date, and benchmark publication date recorded.
- [ ] Historical exposure risk recorded as low / medium / high / unknown with
      justification (a label is a judgment, not proof of (non-)exposure).
- [ ] Whether the case was collected after the evaluated model version's public
      release recorded.
- [ ] Whether live web or repository retrieval was enabled during evaluation recorded.
- [ ] Recorded separately from task-surface leakage (not merged into one score).

Historical exposure verified by: __________________  Date: __________

## 7. Mutation
- [ ] Mutation run recorded with the mutation limit and the viable-mutant count.
- [ ] Kill rate recorded, or "zero viable mutants" recorded explicitly.
- [ ] Zero mutation evidence (if any) is not presented as a measured kill rate.
- [ ] No mutants were manufactured and no hidden tests were added.
- [ ] Any test-scope change affecting the mutation result is documented.

Mutation verified by: __________________  Date: __________

## 8. Licensing
- [ ] Upstream SPDX identifier and license-file blob SHAs at the pinned commit
      recorded.
- [ ] Exact pinned license texts vendored (all files for dual-licensed projects).
- [ ] Any upstream `NOTICE`, `AUTHORS`, data-license, fixture-license, or
      generated-content requirement checked and handled.
- [ ] Per-case third-party notice recorded; no third-party code relicensed.

Licensing verified by: __________________  Date: __________

## 9. Deterministic rebuild
- [ ] Two consecutive rebuilds produce byte-identical pack content and an identical
      `pack.sha256`.
- [ ] License and notice files are covered by `pack.sha256`.

Deterministic rebuild verified by: __________________  Date: __________

## 10. Control behavior
- [ ] `reference-patch` validates the case.
- [ ] Bad, malformed, and no-patch controls do not validate the case.
- [ ] Keyword-gamer does not obtain a validated repair.
- [ ] Fixture-bound controls are not treated as general oracles.

Control behavior verified by: __________________  Date: __________

## 11. Final admission decision

Decision (one of): accepted / hold / rejected / deprecated: ______________
Acceptance level (if accepted): provisional / paper-grade: ______________
Reason code (if hold/rejected/deprecated): ______________________________
Builder: __________________  Date: __________
Independent reviewer (required for paper-grade; a real person, not the builder or any
automation/model): __________________  Date: __________
Unresolved builder/reviewer disagreements: ______________________________
Adjudication outcome: ___________________________________________________

Admission decision by: __________________  Date: __________
