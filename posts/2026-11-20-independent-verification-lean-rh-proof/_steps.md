| # | Step | What It Establishes | Status | Evidence |
|--:|---|---|---|---|
| 1 | Fresh VM | A new Debian 13 VM (22 vCPU, 106 GB RAM) with its own kernel; the build user has no sudo. | ✅ Done | Base image SHA-512 matches Debian's published `SHA512SUMS`. |
| 2 | Toolchains | Lean v4.33.1 (build, export) and v4.36.0 (judge) match the official release tarballs. | ✅ Done | `v4.33.1: installed toolchain matches verified tarball (17493 files)`; v4.36.0: 18248 files. |
| 3 | Checker tools | lean4export, lean4lean, con-leche, con-ron, nanoclo, Pestka and landrun cloned at pinned commits and built. | ✅ Done | Commits listed under *Provenance*. |
| 4 | Project archive | Downloaded inside the VM, verified, extracted read-only. | ✅ Done | `Archive checksum OK (9631b4f0…c7fc)`; `Extracted 175190 files into lean/ (read-only).` |
| 5 | Dependencies | Mathlib and 8 packages cloned at the revisions the project pins; no prebuilt files. | ✅ Done | `mathlib at pinned 0df444a3`; all worktrees clean; `oleans present in packages (should be 0): 0`. |
| 6 | Network cut | VM restarted in isolated mode; nothing after this point can reach the internet. | ✅ Done | `curl: (6) Could not resolve host: github.com`; ping blocked. |
| 7 | Mathlib from source | Built from source with the network off, then compared with Mathlib's official cache. | ✅ Done | 32 min, 0 errors. 8,689 of 8,700 cache oleans byte-identical; 10 are the cache tool itself; 1 differs (see *Findings*). |
| 8 | Challenge export | The five statements, built and exported before any project code ran. | ✅ Done | The community's `Challenge.lean`, built with this Mathlib, exports to exactly `bd484ac9…b2b9`. |
| 9 | Sandbox | Landlock (landrun) confinement for everything that loads project code, tested before use. | ✅ Done | Positive control passes; writes to sources (even after `chmod`), writes outside the build dir, `~/.ssh`, TCP: all denied. |
| 10 | Project build | All 175,187 project modules compiled inside the sandbox (`lake build`). | ⏳ Running | 52,820 / 175,187 modules (30.15%), 7h20m elapsed, ~7,193/h, rough ETA 17.0 h; errors 0, `sorry` warnings 0 |
| 11 | Export | The compiled proof written out as one file (`lean4export`) for the checkers. | ⏸ Pending |  |
| 12 | Comparator | Statements match the challenge; only the 3 standard axioms; Lean kernel + paranoid + nanoda replay. | ⏸ Pending |  |
| 13 | Secondary checks | Axiom audit, per-module `leanchecker` replay, sources unchanged, tools unchanged. | ⏸ Pending |  |
