# Licensing

## Dataset metadata and automation

The original dataset metadata and automation in this repository (import
specifications, evidence documents, the rebuild script, CI, and documentation) will
receive an explicit project license **before any public release**. Until then it is
unlicensed-pending and should be treated as all-rights-reserved by the author.

## Vendored third-party source and tests

This repository does **not** apply one blanket license to vendored third-party
source code. Each benchmark pack vendors source and test files from upstream
projects, and those files remain under **their upstream licenses**, exactly as in
effect at the pinned commits used to build the pack.

- Each pack carries its own exact notices and license texts under
  `packs/<pack>/licenses/`.
- Each pack records, per case, the upstream project, repository, pinned commits,
  applicable license files, and the files it includes, in
  `packs/<pack>/THIRD_PARTY_NOTICES.md`.
- The original per-file copyright and SPDX notices in the vendored files are
  preserved as-is.

**No third-party content is relicensed by this repository.** The notices are a
redistribution record, not legal advice.
