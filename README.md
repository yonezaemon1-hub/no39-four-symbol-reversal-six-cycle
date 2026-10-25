# Four-symbol reversal detection on a homogeneous six-state cycle

Research Note No.39, version 0.4, 25 October 2026.

Ryutaro Yonezu, Yonezu Research Lab.

Repository: https://github.com/yonezaemon1-hub/no39-four-symbol-reversal-six-cycle

Zenodo version DOI: https://doi.org/10.5281/zenodo.23640324

**Unrefereed, AI-assisted preprint. Historical novelty: INCONCLUSIVE.
References: PARTIAL. No priority or first-discovery claim. All rights reserved.**

For the stationary continuous-time homogeneous six-cycle with clockwise rate
`a>0`, counterclockwise rate `b>0`, binary vertex labels `001011`, and equally
spaced observations, the paper derives the exact difference between the
population probabilities of the consecutive words `0011` and `1100`.
A positive polynomial factor proves that this one four-symbol pair witnesses
every nonresonant time-reversal asymmetry in this model. At the resonances,
the entire observation process is reversible. Length four is sharp because
stationary binary words of lengths one through three are reversal symmetric.

The length-three obstruction and eventual reconstruction implications are
established prior context. The exact four-word formula is presented as a
proved result in the specified model, without asserting historical novelty.
It is not a guarantee from one observed four-bit sample, a sample-complexity
bound, or a theorem about general hidden Markov models.

## Files

- [English paper PDF](paper/No39_Four_Symbol_Reversal_v0_4.pdf)
- [LaTeX source](paper/No39_Four_Symbol_Reversal_v0_4.tex)
- [Audit status and later review receipt](AUDIT_STATUS.md)
- [Unchanged audited candidate](audit_candidate_v0_4/README.md)
- [Source-access comparison and remaining limits](audit_candidate_v0_4/PRIOR_COMPARISON.md)
- [Original audited ZIP](No39_Four_Symbol_Reversal_Search_v0_4_20261025.zip)

The original candidate archive is preserved byte for byte, including its
historical preparation-stage labels. The later review and publication state
are recorded separately here. The PDF typesets the same theorem and proof;
its review-status note reflects the later source confirmation.

## Offline reproduction

In `audit_candidate_v0_4`, run:

```powershell
python check_hashes.py
python -I verify.py --output rerun.json
python -I audit_positivity_dense.py --output positivity_rerun.json
```

Python 3.10 or newer; standard library only. The four programs are byte-identical
to the reviewed candidate. Their implementation version label remains v0.2.
The fixed `EXTERNAL PROOF AUDIT NOT RUN` line is not a live summary of later
received AI reviews; see AUDIT_STATUS.md. Numerical diagnostics supplement
the exact identities and analytic proof.

The Windows receipt is a reported Python 3.12.10 run of the identical v0.2
implementation, with 15 manifest entries. It does not certify the later
document sets. The frozen v0.4 candidate manifest has 32 entries.

## Research status

Received AI reviews report independent proof derivation and subsequent
acceptance of the reflection clarification. The FTY appendix's explicit
shift-only statement was verified separately against the author-hosted source.
These are scoped AI-assisted checks, not human journal or conference peer
review. Reviewer SciPy programs and raw data were not supplied.
Howard's periodic-scenery full text and the final Matzinger-Rolles article
remain unchecked; literature coverage does not establish historical novelty.

Research inquiries and earlier overlapping work:
**yonezaemon1+research@gmail.com**.

Copyright (c) 2026 Ryutaro Yonezu. All rights reserved.
No MIT, Apache, CC BY or other general reuse license is granted.
