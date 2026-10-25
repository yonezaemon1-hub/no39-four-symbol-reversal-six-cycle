# Received independent AI proof-review report — No.39 v0.3

Received 25 October 2026. The reviewed object was
No39_Independent_Proof_Review_20261025.zip, not the full v0.3 candidate archive.
Its PROOF.md was a byte-identical copy of the v0.3 mathematical note.

The supplied review reports re-deriving Sections 1-5 without the packaged
code. It reports hand derivation of the spectrum and inverse Fourier kernel,
exact symbolic verification of the signed four-word formula and the
stationary triple-product route, and exact positivity calculations. It also
reports a 5,000-point scipy.expm check with error at most 1e-16, finite
resonance checks through length ten, and labeling diagnostics. These are
received claims: the reviewer's code, seeds, point sets and raw outputs were
not supplied here. They are not newly reproduced experiments in v0.4.

## Verdict as received

| Item | Received verdict | Scope / condition |
| --- | --- | --- |
| 1. Generator and kernel | PASS | Spectrum, six kernel formulas and normalization |
| 2. Four-word formula | PASS | Exact signed identity by two derivations; numerical check also reported |
| 3. Positivity | PASS | Quadratic minimum, seven Bernstein coefficients, case split and factorization |
| 4. Every-length resonance | PASS | Circulant symmetry and hidden-path reversal; finite tests are supplementary |
| 5. Shortest word length | PASS | Stationary binary words of lengths one through three |
| 6. Labeling | CONDITIONAL PASS | Make time reversal = rate exchange and label-preserving reflection explicit |
| 7. FTY and interpretation | CONDITIONAL PASS | Identify the shift-only appendix theorem and clarify source-version / footnote numbering |

The review did not assess novelty, broader literature coverage, or publication.
It describes an AI proof review, not human peer review. It says its FTY check
used a summary of the original rather than a full-paper inspection.

## Response in v0.4

PROOF Section 5 now explicitly identifies P_{a,b}^T=P_{b,a} and the
label-preserving reflection. Section 6 fixes the author-hosted manuscript
dated 30 March 2014 and refers directly to Theorem Appendix A.1 and its
proof in Appendix A.3. In that inspected manuscript the footnote is 3.
The report's arXiv footnote number 1 remains a received claim; versioned
arXiv PDF access failed in this pass. No error is inferred merely from a
difference between editions.

These responses address the stated requests. They do not retroactively change
the received verdicts to seven PASS results; the revised text has not yet
received a new independent review.

## Package observations and their scope

- The old independent-review packet omitted RECEIVED_NUMERICAL_REVIEW.md,
  although PRIOR_ART.md referred to it. The full v0.4 archive includes that
  report; no proof or current-document file reference is intentionally missing.
- The old review-packet manifest had 16 entries; the full v0.3 package had
  22. These are different archives, not a contradiction.
- The Windows receipt concerns v0.2, 15 manifest entries, Python 3.12.10.
  Only its byte-identical computational implementation carries forward.
  It does not establish a Windows hash check of the v0.4 document set.
- The review reported that the proof-core hash matched the old packet's
  PACKAGE_PROVENANCE.json, and that all three packaged checkers passed.
  Program execution is distinguished from the reported independent derivation.

No external publication or reviewer contact is performed by this revision.
