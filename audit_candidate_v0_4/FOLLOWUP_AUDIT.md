# No.39 v0.2 follow-up — 25 October 2026

## Outcome

The received numerical report is recorded in RECEIVED_NUMERICAL_REVIEW.md
without converting it into a proof audit. A separate rational implementation
passes all eight exact checks listed below. The previously missing primary
Matzinger--Lember manuscript was obtained and compared; version and access
limits are in PRIOR_ART.md. Novelty remains INCONCLUSIVE.

## Separate exact positivity check

`audit_positivity_dense.py` imports neither `verify.py` nor `exact_algebra.py`.
It uses dense univariate Fraction arithmetic. Instead of deriving Bernstein
coefficients with the original forward conversion formula, it directly
expands the proposed Bernstein basis polynomials and compares ordinary power
coefficients in the reverse direction.

| Exact check | Outcome |
| --- | --- |
| Expansion of the seven Bernstein terms equals q(3u/4) coefficient by coefficient | PASS |
| Bernstein basis polynomials sum to 1 | PASS |
| All seven proposed coefficients are strictly positive | PASS |
| Completing the square gives 4AC-B^2=4r^2 q(r^2) | PASS |
| G(r,1)=(1-r)^2(r^6+3r^4+6r^3+5r^2+2r+1) | PASS |
| Derivative of r+r^5-4+4r^2 equals 1+8r+5r^4 | PASS |
| Boundary sign: (25/32)^2*3-1=851/1024>0 | PASS |
| G(1,1)=0, confirming the strict-positivity domain excludes r=1 | PASS |

The inequalities completing the argument are analytic: on 0<=u<=1,
the Bernstein weights are nonnegative and sum to 1. On r^2>=3/4,
the positive derivative and the exact threshold sign put the quadratic vertex
above c=1; the positive endpoint factorization then controls -1<=c<=1.
There is no uncovered point at r^2=3/4, since both arguments apply there.

These checks validate the stated positivity proof internally. They are not
an independent external mathematical review, nor a new proof of the full
four-symbol theorem from scratch.

## Original mathematical content

The statement, formulas and proofs in Sections 1-5 of PROOF.md are byte-identical
to the corresponding v0.1 text. Their common SHA256 is recorded in CHANGES.json.
The original v0.1 archive is preserved verbatim in history/original_v0_1.zip.
Its original eight-file hash manifest and evidence remain inspectable there.

`exact_algebra.py` is byte-identical to v0.1. In `verify.py`, changes are the
explicit local-module path for -I and review/version labels only.

## Remaining decisions

The candidate residual remains the explicit one-pair, four-consecutive-symbol
sufficiency result for the specified homogeneous six-state cycle. The generic
binary lower bound, eventual distinguishability from spectral reconstruction,
and sampling ambiguity remain attributed to prior work.

An independent mathematical reviewer still needs to assess the full argument.
The scoped literature comparison has been improved but does not establish
priority or scholarly novelty. No external publication was performed.
