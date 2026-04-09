# Admission checklists

One file per case, pre-filled with everything that can be measured.

Each file follows [`../case-admission-checklist.md`](../case-admission-checklist.md).
The `>` quoted blocks hold facts derived from the upstream Git objects and from this
repository's CI: tree SHAs, changed paths, the regression test, the certification
verdict, the mutation result, and the license blob SHAs.

**The tick boxes and initials are deliberately blank.** These files record what was
measured, not that anyone reviewed it. The protocol is explicit that automation cannot
sign a section, so nothing here is signed.

## How to use them

Read a file, satisfy yourself the measured facts are right, tick the boxes and initial
the sections. Two labels are judgments no measurement can supply, and both are marked
in the file: task-surface leakage risk, and historical exposure risk.

Signing every section as the builder gives a case **provisional** acceptance.
**Paper-grade** additionally needs a second real person, other than the builder, to sign
the provenance, historical evidence, regression, leakage, exposure and licensing
sections. Until that happens the case stays provisional, which is what the pack
currently claims.
