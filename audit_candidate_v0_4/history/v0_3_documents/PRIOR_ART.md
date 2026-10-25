# No.39 scoped prior-art check — 25 October 2026

## Decision

NOVELTY: INCONCLUSIVE. REFERENCES: PARTIAL.

The explicit, sharp four-consecutive-symbol sufficiency statement is a
candidate residual. The broader mechanisms and the eventual-detection
dichotomy are established context or direct consequences and are not claimed
as discoveries. No claim of exhaustive coverage is made.

## Primary texts actually inspected

| Source | Access and relevant location | Consequence for this candidate |
| --- | --- | --- |
| Arola-Fernandez--Lacasa (2023), arXiv:2303.11868 | PDF, Section III.A, pp.4-5; example `0010110010` on p.5 | The binary word-length lower bound and short asymmetric symbolic examples are known. |
| Finucane--Tamuz--Yaari (2014), author-hosted scenery.pdf | PDF, Introduction and Theorem 1.2; Appendix A theorem argument | Coefficients must be distinct as complex values; Definition 1.1 is shift-only. Eventual detection follows. |
| Bauer--Seifert--van der Meer (2025), arXiv:2412.15642v2 | Full HTML, especially Section 3.2.2, equations (30)-(33) | Periodic-sampling ambiguity between generators and equilibrium/nonequilibrium is established. |

URLs and bibliographic details are in PROOF.md. Only relevant passages were
analyzed; no full independent re-audit of these papers is claimed.

## Newly recovered primary manuscript

Matzinger--Lember: university preprint 05007 (15 pages, submitted 2005),
linked by the university record to the 2006 SPA publication.

https://sfb701.math.uni-bielefeld.de/preprints/view/7
https://sfb701.math.uni-bielefeld.de/preprints/sfb05007.pdf

Sections 2, 3.1-3.5.1 and 4 were inspected. Equivalence identifies shifts and
reflections. Theorem 3.2 supplies a spectral reconstruction criterion.
Example 3.1 (printed pp.12-13) uses period six, equal probabilities for jumps
+1 and +2, and includes labeling 110100, the reversal of 001011.
The examined statements do not give the continuous-time four-consecutive-word
formula. Our inference is that these statements alone do not settle that
specific residual. This is not a global novelty finding. The final publisher
PDF returned 403 and was not compared against this earlier manuscript.
Howard's earlier full texts remain outside the completed comparison.

## Search coverage and limits

The initial searches covered binary hidden Markov time reversal, irreversibility
on colored cycles, random-walk scenery reconstruction, stroboscopic Markov
sampling, and four-point/length-four reversal statistics. Follow-ups used
`001011`, `0011`, `six-state`, `circulant`, `four-point`, and `sampling` in
combinations with time reversal or irreversibility. Two search engines were
used. Exact-phrase searches were frequently sparse or irrelevant.

The follow-up also traced a sample-complexity citation to Matzinger--Rolles
(2003), Reconstructing a piece of scenery with polynomially many observations.
That text has not been fully compared; no conclusion about its complete
scope is claimed.

The search established that the general topic and all-length distinguishability
are occupied. It did not establish historical novelty for the explicit witness
formula. Unread texts, alternate formulations, and immediate consequences of
other finite-HMM results remain possible. A final novelty statement should
stay INCONCLUSIVE unless that comparison is materially extended.

## What an adversarial audit should try to break

1. Verify the clockwise sign convention in the six Fourier eigenvalues and
   in p(0011)-p(1100).
2. Expand the two probabilities directly, independently of exact_algebra.py.
3. Check the Bernstein certificate and the split at r^2=3/4.
4. Try to find a nonresonant zero for the four-word difference.
5. Check that no nonstationary, heterogeneous-rate, unequal-spacing,
   finite-sample, or general-HMM conclusion has been silently added.
6. Search the scenery and HMM literature for this specific consecutive
   length-four witness before considering a priority claim.

An external numerical review report is now recorded in
RECEIVED_NUMERICAL_REVIEW.md. Its code and raw data were not supplied, and it
explicitly did not independently derive the proof or check novelty. The
separate dense-rational checker in v0.2 is an internal cross-check, not
independent peer review.

## v0.3 clarification

The FTY author-hosted PDF was checked again at Definition 1.1, Theorem 1.2,
and footnote 3. Section 6 now spells out complex-value distinctness and the
shift-only convention. No new novelty conclusion is drawn. The user's separate
arXiv-based check is recorded as a received report, not a byte comparison
performed by this revision.
