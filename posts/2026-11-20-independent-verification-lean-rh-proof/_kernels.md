| Checker | By | What It Is | Verdict | Time | Peak RAM | Evidence |
|---|---|---|---|--:|--:|---|
| Lean kernel (C++) | Lean FRO | The reference kernel, replaying the export inside `lake comparator`. | ⏸ Pending |  |  |  |
| Lean kernel, paranoid mode | Lean FRO | The same kernel with extra internal checks. | ⏸ Pending |  |  |  |
| nanoda | Chris Bailey | Independent kernel in Rust. | ⏸ Pending |  |  |  |
| con-leche `--compare` (from `.olean`) | Lean FRO | Formally verified checker reading the compiled files directly and comparing the statements with the challenge (built from the trusted, pre-project Mathlib). Needs no export. | ✅ Accepted | 19:29.73 | 33.3 GB | `accepted 750237 declarations, 5 axioms justified by the solution Main (2660207 declarations accepted) (--verified)`; 5 of 5 theorems: `justified by the solution` |
| con-leche `--compare` | Lean FRO | Formally verified checker; also re-does the statement comparison. | ⏸ Pending |  |  |  |
| con-leche | Lean FRO | Formally verified: anything it accepts has a model in set theory. | ⏸ Pending |  |  |  |
| con-ron | Lean FRO | Rust port of con-leche. | ⏸ Pending |  |  |  |
| lean4lean | Mario Carneiro | Kernel written in Lean, partly verified; run module by module. | ⏸ Pending |  |  |  |
| Pestka | jasisz | Independent kernel written in Aver. | ⏸ Pending |  |  |  |
| nanoclo | sgraf812 | Independent Rust kernel, forked from nanoda. | ⏸ Pending |  |  |  |
