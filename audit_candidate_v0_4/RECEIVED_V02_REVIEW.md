# Received v0.2 review report — 25 October 2026

Source: the additional audit text supplied by the user in this conversation.
The report describes a separate implementation in the conversation, not an
external journal/conference review. Programs, random seeds, parameter points
and raw outputs were not supplied. This revision records the reported results;
it does not claim to have rerun the 20,000-point SciPy experiment.

## Reported outcome

Mathematics, numerics and package integrity: PASS within the stated checks.
Novelty and publication decision: held open by the reviewer.

| Check | Result reported for v0.2 |
| --- | --- |
| check_hashes.py | 15 files PASS |
| verify.py with -I; audit_positivity_dense.py | PASS |
| Comparison with v0.1 | exact_algebra.py and PROOF Sections 1-5 unchanged |
| Separate scipy.linalg.expm, 20,000 random rate/spacing points | Absolute formula error <=1.4e-16; clockwise convention and sign matched |
| G on a grid | Smallest sampled value about 1.8e-11 near r=1 |
| G at random points | Smallest sampled value about 1.9e-5 |
| G(r,1)/(1-r)^2 | Reported sampled minimum about 4.2; see the domain clarification below |
| Quadratic completion | Numerical agreement at r=0.2,0.5,0.8 |
| q on 0<=t<=3/4 | Minimum reported as q(3/4)=535/4096 |
| Case-split boundary | Both branches apply at r^2=3/4 |
| All 64 binary labelings, generic nonresonant inputs | 12 chiral labelings first asymmetric at length 4; remaining 52 symmetric through length 5 |
| Resonances m=1,2,3 | Tested word lengths through 8; differences around 1e-16 |
| FTY source check | Shift-only Definition 1.1 and complex-valued distinctness in Theorem 1.2 confirmed by the reviewer |

The statement about all lengths is supplied by the analytic argument in
PROOF.md; the finite word tests alone do not prove it. Likewise a positive
sampled minimum is not a proof over a continuous domain.

## Clarification of the normalized endpoint minimum

The reported value 4.2 is retained only as a sample-dependent observation.
The tested r range and raw points were not supplied. It cannot be a minimum
over the full interval 0<r<1. Exact factorization gives

$$H(r)=\frac{G(r,1)}{(1-r)^2}
=1+2r+5r^2+6r^3+3r^4+r^6.$$

Thus 1<H(r)<18 for 0<r<1, with infimum 1 as r tends to zero.
For example, H(1/2)=269/64=4.203125. No sample range is inferred from this
example. This clarification does not affect the positivity theorem.

## Limits explicitly maintained

- The report does not independently derive the full proof and is not external peer review.
- It does not verify the earlier 3,000-point report's absent code or data.
- Historical novelty remains INCONCLUSIVE; Howard and final-version comparisons remain incomplete.
- Four-symbol sufficiency is a statement about probabilities, not a one-sample decision or sample-complexity guarantee.
- No Windows-machine rerun was reported; the supplied package evidence is from Linux.
