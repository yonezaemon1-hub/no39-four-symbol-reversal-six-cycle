# Scoped prior-art comparison — No.39, 25 October 2026

## Outcome

**REFERENCES: PARTIAL. NOVELTY: INCONCLUSIVE.**

The remaining candidate is only the explicit p(0011)-p(1100) formula and
its sharp four-consecutive-symbol sufficiency for the specified sampled
homogeneous six-cycle. This pass improves source coverage but does not
exclude all older implications. The theorem is unchanged. Version 0.4 adds
an explicit reflection argument and pins the FTY source; its two received
conditional review items have not been independently re-reviewed.

## Material actually available

| Work | Access in this pass | Relevant scope and comparison |
| --- | --- | --- |
| Matzinger–Rolles, SPA 107 (2003), 289-300, Reconstructing a piece of scenery with polynomially many observations | Publisher-indexed and university-hosted abstract; publisher 403; author-linked mediaTUM record 429; final journal PDF still unavailable | Reconstructs finite pieces of iid scenery on Z with high probability from polynomially many observations; reflection and translation are allowed. This concerns reconstruction/sample complexity, not a fixed word-probability witness. |
| Matzinger–Rolles, EURANDOM 2002-010, Reconstructing a random scenery in polynomial time | Complete 11-page institutional PDF obtained; main result and Setting inspected, with an additional proof passage | A related earlier text under a different title. It assumes iid uniform scenery, a recurrent walk with finite increment support and reachability on Z. No line-by-line equivalence to the final 2003 article is established. |
| Howard, Random Structures & Algorithms 8 (1996), 59-74, Detecting defects in periodic scenery by random walks on Z | Publisher abstract; PDF route returned to abstract; author page unavailable | Treats periodic scenery and finite defects for symmetric walks, plus a stronger purely periodic result for asymmetric walks, with increments restricted to {-1,0,+1}. Full theorem/proof comparison remains incomplete. |
| Howard, Combinatorics, Probability and Computing 5 (1996), 247-256, Orthogonality of measures induced by random walks with scenery | Publisher abstract | Describes distinguishability for simple walks when some color has a finite nonempty preimage. The full article was not obtained. |
| Howard, Statistics & Probability Letters 34 (1997), 123-132, Distinguishing certain random sceneries on Z via random walks | Primary publisher-indexed abstract fragment only; publisher PDF returned 403 | The indexed abstract describes a fixed-versus-random scenery result. No full-text exclusion or theorem-level comparison is claimed. |

## Direct-applicability checks

### Matzinger–Rolles

The reconstructed object, underlying space, and quantifiers differ from No.39.
A deterministic periodic binary labeling is a probability-zero family under
an iid nontrivial coloring of Z. An almost-sure theorem under that random
scenery law cannot be instantiated at this fixed labeling without a further
argument. Recovering an unknown finite scenery piece from many observed colors
also differs from finding the smallest consecutive-word length whose population
probabilities distinguish a process from its reversal.

This is our model comparison, not a claim that no lemma or extension of those
works could imply the candidate. The 2002 text is retained as a separately
identified precursor, not silently substituted for the final 2003 journal text.
Some old-font mathematical glyphs in its extracted text are corrupted, so this
report does not transcribe its precise polynomial exponents or alphabet-size
inequality from those glyphs. The main iid/recurrent/finite-support assumptions
are stated in readable prose in Sections 1-2.

### Howard's periodic-scenery result

The nearest-neighbor restriction in the available abstract is not a direct
match to No.39's sampled propagator. Between two samples the continuous-time
chain may make several jumps. In fact, for a,b,tau>0 and j=0,...,5,

$$P_\tau(0,j)\ \geq\ e^{-(a+b)\tau}\frac{(a\tau)^j}{j!}\ >0,$$

using the event of exactly j clockwise jumps and zero counterclockwise jumps.
Thus the sampled chain has all six modular displacements in its support.
Replacing sampled observations with the colors at every individual jump would
give additional data and would require justification. The available abstract
therefore cannot simply be applied as the same sampled model. Whether the
unavailable proof gives a broader reduction or this special four-word identity
remains unchecked.

For the other 1996 Howard abstract, a nonconstant periodic coloring on Z has
infinite preimage for each color that appears. Its stated finite-marker
hypothesis does not directly describe the No.39 labeling. This comparison is
limited to the abstract, not to every result in the article.

## Sources and version/access limits

- Matzinger–Rolles final publication metadata and abstract:
  https://www.sciencedirect.com/science/article/pii/S0304414903000851
  https://research.tue.nl/en/publications/reconstructing-a-piece-of-scenery-with-polynomially-many-observat/
  DOI: 10.1016/S0304-4149(03)00085-1.
- Institutional 2002 report index and text:
  https://www.eurandom.tue.nl/pre-prints-new/
  https://www.eurandom.tue.nl/reports/2002/010-report.pdf
- Howard periodic scenery, publisher abstract:
  https://onlinelibrary.wiley.com/doi/abs/10.1002/(SICI)1098-2418(199601)8:1%3C59::AID-RSA3%3E3.0.CO;2-Q
- Howard orthogonality, publisher abstract:
  https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/orthogonality-of-measures-induced-by-random-walks-with-scenery/439ED598C2F1B9454B1FC41A3CD00F87
  DOI: 10.1017/S0963548300002017.
- Howard 1997 publisher record/PDF index:
  https://www.sciencedirect.com/science/article/pii/S0167715296001733
- Author publication page attempted but unavailable in this pass:
  https://mfeapp.baruch.cuny.edu/math/doug/

The previously inspected Matzinger–Lember manuscript remains a preprint-stage
comparison, not a check of the typeset final version. Finucane–Tamuz–Yaari's
shift-only reconstruction criterion remains the established source of the
all-length consequence; see PROOF Section 6. No full third-party paper PDFs
are redistributed in this package.

## Additional v0.4 access checks

The FTY comparison fixes the author-hosted manuscript dated 30 March 2014;
see the source locations in PROOF Section 6 and PRIOR_ART.md. The arXiv record
lists v1 (27 May 2011) and v2 (30 April 2014), but both versioned PDF routes
were inaccessible here. The received report's arXiv footnote number was not
independently confirmed; the author manuscript's footnote is 3.

For Matzinger–Rolles, the current TUM author publication list led to the
mediaTUM record below and the publisher DOI. The record returned 429 and the
publisher article returned 403. An archived author publication-list link was
also unavailable. Matzinger's Georgia Tech research page led to a 491-page
habilitation manuscript. Its contents and target-title search hits were
inspected, but they did not provide an identified copy of the final 2003
article. Related texts are not substituted for that final article.

- Author publication list:
  https://www.math.cit.tum.de/en/math/people/professors/rolles-silke/
- Author-linked record (429 in this pass):
  https://mediatum.ub.tum.de/node?change_language=en&id=1662823
- Archived author page:
  https://www.mathematik.uni-muenchen.de/~math/archiv/2007/stochast/download/pers/srolles/index.html
- Matzinger's research page and related manuscript:
  https://matzi.math.gatech.edu/scenery.html
  https://matzi.math.gatech.edu/heinihabil.pdf

For Howard, the official author publication list was visible in search-indexed
text, while direct retrieval timed out. The publisher's PDF link again
redirected to the abstract. The indexed list confirms bibliography, not access
to the periodic-scenery proof. Full-text comparison remains incomplete.

## Remaining boundary

Do not label this pass as historical-novelty clearance. The direct hypotheses
of the inspected statements do not supply the No.39 four-word conclusion as
written, but indirect equivalences, unread lemmas, the final journal versions,
and other literature remain possible. Priorities and publication remain open.
