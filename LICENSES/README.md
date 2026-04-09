# Licensing

Two different things live in this repository, under two different licenses.

## What we wrote

The import specifications, evidence documents, rebuild script, CI, and documentation
are **MIT licensed**. See [LICENSE](../LICENSE) at the repository root.

## What we vendored

Each case ships source and test files copied from an upstream project. Those files
stay under **their own upstream licenses**, exactly as they stood at the commit the
case was built from. We do not relicense them, and we do not put one blanket license
over them.

For every pack:

- The full upstream license texts are in `packs/<pack>/licenses/`.
- `packs/<pack>/THIRD_PARTY_NOTICES.md` records, per case, the upstream project, its
  repository, the pinned commits, which license files apply, and what was included.
- Per-file copyright headers and SPDX identifiers in the vendored files are left
  exactly as they were.

The notices are a record of what was redistributed and under what terms. They are not
legal advice.
