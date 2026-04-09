# Admission checklists

One completed checklist per case, following
[`../case-admission-checklist.md`](../case-admission-checklist.md).

The `>` quoted blocks hold facts derived from the upstream Git objects and from this
repository's CI: tree SHAs, changed paths, the regression test, the certification
verdict, the mutation result, and the license blob SHAs. The builder has reviewed
those facts and signed each section.

All 25 cases are **accepted** at the `provisional` level. Reaching `paper-grade`
additionally requires a second reviewer who is not the builder, so the
independent-reviewer line is left for that person to sign.

## The two judgment labels

No measurement supplies these, so both are recorded with the reasoning behind them.

**Task-surface leakage.** `medium` where an upstream test name echoes a ground-truth
concept, `low` otherwise. Two cases are medium:
`click_shared_default_precedence_001` (upstream's `test_shared_param_prefers_first_default`
against the concept "order-sensitive default") and `rich_table_padding_width_001`
(upstream's `test_padding_width` against "cell padding width"). Both names are
upstream's own and were not renamed to satisfy the contamination lint.

**Historical exposure**, from the date the upstream fix became public:

| Fix date | Label | Cases |
|---|---|---:|
| before 2023-01-01 | high | 7 |
| 2023-01-01 to 2025-08-31 | medium | 4 |
| 2025-09-01 or later | low | 14 |

A label is a statement about dates, not proof that a model did or did not see the fix.

## Getting a case to paper-grade

A second person, who is not the builder and is not automation, signs the provenance,
historical evidence, regression, leakage, exposure and licensing sections. Until then
the case stays provisional, which is what the pack claims.
