# No.39 v0.3 — explanatory revision

25 October 2026. The theorem, its mathematical proof in Sections 1-5, and
all verification programs are unchanged from v0.2. No new numerical experiment
was run for this documentation revision.

## FTY wording

PROOF Section 6 now explicitly separates four groups with distinct moduli
from the requirement that all six Fourier coefficients be pairwise distinct
as complex numbers. The two values in a conjugate pair have equal modulus.
Their complex values are different when sin(theta)!=0.

The shift-only definition is stated explicitly, so reflection is not silently
quotiented out. The known-consequence interpretation and the narrow candidate
refinement remain the same. Source access is recorded in PRIOR_ART.md.

## Review record and a numerical-domain clarification

RECEIVED_V02_REVIEW.md records the supplied 20,000-point report as reported,
without labeling it external peer review or inventing missing raw evidence.
The earlier 3,000-point report remains unverified at the raw-code/data level.

One sample statistic required a domain qualification: the reported minimum
4.2 of G(r,1)/(1-r)^2 is not a global lower bound. The exact polynomial is

$$H(r)=1+2r+5r^2+6r^3+3r^4+r^6.$$

Its derivative 2+10r+18r^2+12r^3+6r^5 is strictly positive for r>0.
Consequently its infimum on 0<r<1 is 1, approached at r=0, and its
supremum is 18, approached at r=1. Neither endpoint is in the domain.

The report's value min q=535/4096 on [0,3/4] is consistent with the exact
Bernstein certificate: every coefficient is at least 535/4096 and the last
coefficient has that value, attained at the upper endpoint. No correction
to the positivity proof is needed.

## Status

- Received mathematical/numerical checks: reported PASS within their stated scope.
- Packaged exact and numerical implementations: unchanged from the tested v0.2 versions.
- Independent external proof audit: not performed.
- References: PARTIAL; novelty: INCONCLUSIVE.
- External publication: not performed; no new publication decision is inferred.

The old v0.2 explanatory files are preserved in history/v0_2_documents.
The byte-identical original v0.1 archive remains in history/original_v0_1.zip.
CHANGES.json records comparison hashes and the revision scope.
