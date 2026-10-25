# Four-symbol reversal detection on a homogeneous six-state cycle

Research candidate No.39, v0.4, 25 October 2026.

This is a working mathematical note, not a released paper. An AI proof-review
report was received for v0.3: it reports independent re-derivation of Sections
1-5, with five PASS and two CONDITIONAL PASS assessments across seven review
items. The report and its limits are recorded in RECEIVED_PROOF_REVIEW_V03.md;
the reviewer's programs and raw outputs were not supplied. This is not human
peer review. Earlier numerical reports and internal exact checks remain
separately identified. Version 0.4 makes the reflection argument explicit and
pins the FTY source and Appendix A reference. The theorem and computational
implementation are unchanged. Historical novelty is INCONCLUSIVE and no
priority claim is made.

## 1. Model and statement

Let X(t) be a continuous-time nearest-neighbor Markov chain on Z/6Z, with
clockwise rate a>0 and counterclockwise rate b>0 at every vertex. The initial
distribution is uniform. Set f=(0,0,1,0,1,1) in clockwise vertex order and
Y_k=f(X(k tau)), where tau>0. A word probability p(w) refers to the stationary
law of consecutive Y's, not the reliability of a single observed word.

Put

$$r=e^{-(a+b)\tau/2},\qquad
\theta=\frac{\sqrt3}{2}(a-b)\tau,\qquad c=\cos\theta.$$

**Candidate theorem.** Define

$$G(r,c)=1-2r^2+4r^6+r^8+4r^2(1-r^2)c^2-2r^3(1+r^4)c.$$

Then

$$p(0011)-p(1100)=-\frac{\sqrt3}{54}r^3\sin\theta\,G(r,\cos\theta),$$

and G(r,c)>0 for 0<r<1 and -1<=c<=1. Consequently:

1. If sin(theta) is nonzero, this one pair of length-four words witnesses
   time-reversal asymmetry. No length-one, two, or three consecutive words
   can witness such asymmetry for any stationary binary process.
2. If sin(theta)=0, the entire sampled hidden chain, and therefore its binary
   observation process, is time-reversal symmetric at every word length.

For a!=b the blind spacings are exactly

$$\tau=\frac{2\pi m}{\sqrt3\,|a-b|},\qquad m=1,2,3,\ldots.$$

For a=b all spacings are reversible.

The candidate contribution is the explicit **length-four sufficiency** and
its positive prefactor. The all-length dichotomy also follows from established
scenery reconstruction, as explained in Section 6; it is not an independent
novelty claim.

## 2. Transition kernel and the four-symbol identity

For the row-generator convention,

$$ (Qh)(i)=a(h(i+1)-h(i))+b(h(i-1)-h(i)).$$

The characters exp(2 pi i k i/6) have eigenvalues

$$\mu_k=(a+b)(\cos(2\pi k/6)-1)+\mathrm{i}(a-b)\sin(2\pi k/6).$$

Thus the six eigenvalues of P=exp(tau Q), in character order, are

$$1,\ r(c+\mathrm{i}s),\ r^3(c+\mathrm{i}s),\ r^4,
\ r^3(c-\mathrm{i}s),\ r(c-\mathrm{i}s),\qquad s=\sin\theta.$$

Let K_j=P(0,j). Fourier inversion gives, with d=sqrt(3),

$$6(K_0,K_1,K_2,K_3,K_4,K_5)=$$

$$\big(1+r^4+2rc+2r^3c,\quad
1-r^4+rc+drs-r^3c+dr^3s,\quad
1+r^4-rc+drs-r^3c-dr^3s,$$

$$1-r^4-2rc+2r^3c,\quad
1+r^4-rc-drs-r^3c+dr^3s,\quad
1-r^4+rc-drs-r^3c-dr^3s\big).$$

For D_0=diag(1-f) and D_1=diag(f),

$$p(w)=\frac16\mathbf1^T D_{w_0}P D_{w_1}P\cdots
 P D_{w_{\ell-1}}\mathbf1.$$

Substitution for the two length-four words and use of c^2+s^2=1 gives
the displayed probability difference. This step can be checked by direct
finite expansion: exact_algebra.py enumerates microscopic paths, works over
Q[r,c,s,d]/(d^2-3), and reduces the difference modulo c^2+s^2-1.
The coefficient remainder is identically zero. No numerical approximation
enters this identity.

## 3. Strict positivity of G

View G as a quadratic in c. Its leading coefficient is
4r^2(1-r^2)>0 and its vertex is

$$c_* = \frac{r(1+r^4)}{4(1-r^2)}.$$

First suppose r^2<=3/4 and put t=r^2. The unrestricted quadratic minimum is

$$G(r,c_*)=\frac{q(t)}{4(1-t)},$$

$$q(t)=4-12t+7t^2+16t^3-14t^4-4t^5-t^6.$$

On 0<=t<=3/4 set u=4t/3. The degree-six Bernstein expansion is

$$q(3u/4)=\sum_{j=0}^{6} B_j {6\choose j}u^j(1-u)^{6-j},$$

with

$$ (B_0,\ldots,B_6)=
\left(4,\frac52,\frac{101}{80},\frac58,
\frac{403}{640},\frac{443}{512},\frac{535}{4096}\right).$$

All seven coefficients are strictly positive and the Bernstein basis sums
to one. Hence q(t)>0 throughout this interval, proving G>0 there for all real c.

Now suppose r^2>=3/4. The function

$$r(1+r^4)-4(1-r^2)$$

is strictly increasing for r>0, and at r=sqrt(3)/2 has value
25sqrt(3)/32-1>0. Thus c_*>1. On -1<=c<=1, G decreases as c increases,
so it suffices to consider c=1. Exact factorization gives

$$G(r,1)=(1-r)^2
 (r^6+3r^4+6r^3+5r^2+2r+1)>0\quad(0<r<1).$$

This completes the positivity proof. The coefficient identity, vertex
minimum polynomial, and endpoint factorization are checked over rationals
by verify.py.

## 4. Sharp word length and the resonant case

For any stationary binary process, the length-two identity p(01)=p(10)
follows from equality of one-site marginals. At length three, stationarity
of the word 00 gives p(001)=p(100), and stationarity of 11 gives
p(011)=p(110). All other length-three words are palindromes. These facts
prove the lower bound four without any Markov assumption on Y.
This lower bound is established prior art [1].

If sin(theta)=0, all K_j=K_{-j}, so the sampled chain has symmetric P.
For every hidden path (i_0,...,i_l), uniform stationarity and P=P^T make
its probability equal to that of its reversed path. Summing over hidden
paths with any specified binary labels proves observed reversal symmetry
at every length. If sin(theta)!=0, Section 3 makes the displayed
four-word difference nonzero, establishing the converse.

## 5. Labeling and interpretation limits

A binary labeling f is reflection-symmetric when f(i)=f(k-i) for some k.
For uniform stationarity, the reversed hidden transition matrix is
P_{a,b}^T=P_{b,a}, because Q_{a,b}^T=Q_{b,a}; hence the time-reversed observation
law at rates (a,b) is the forward observation law at rates (b,a). The reflection
sigma(i)=k-i preserves the uniform initial law, interchanges the two rates,
and preserves the observed label whenever f(i)=f(sigma(i)). Thus in this case
the forward laws at (a,b) and (b,a) agree, proving reversibility of the
observations at every tau, irrespective of drift.

Among the 64 labelings on six vertices, 52 have such a reflection and 12
do not. The latter form the two rotational orbits represented by 001011
and 001101. The second is a rotation of the reversed first labeling.
Rotation preserves word probabilities, and reflection interchanges a,b.
Thus the theorem covers every chiral labeling on the six-cycle, with a
possible sign reversal of the witness.

All binary labelings on cycles of lengths 3,4,5 have a reflection. These
small counts are exhaustively verified. The minimal size six is only about
**homogeneous nearest-neighbor cycles with deterministic binary vertex
labels**. It is not a minimal-state claim about general hidden Markov models.

This note addresses stationary statistical time reversal of sampled paths.
It does not say that thermodynamic nonequilibrium is impossible to infer
from other structural information. In particular, at odd resonances the
sampled matrix has negative eigenvalues, obstructing a reversible
continuous-time embedding. At even resonances it equals the sampled
propagator of the symmetric ring with rates a'=b'=(a+b)/2.

Nor does a length-four witness mean that four recorded bits suffice for
a reliable empirical decision. The probabilities need repeated estimation.
Signals may be extremely small near resonances or at large tau.
No finite-sample detection guarantee or dissipation estimator is claimed.

## 6. Established implications and remaining novelty question

For Finucane--Tamuz--Yaari [2], the source fixed here is the author-hosted,
17-page manuscript dated 30 March 2014, not an unspecified arXiv version.
Definition 1.1 (printed p.2) uses shifts only. Theorem 1.2 and footnote 3
(printed p.3) distinguish this convention from Matzinger--Lember's
shift-and-reflection equivalence. The explicit shift-only statement we use
is Theorem Appendix A.1 (printed p.14), with its proof completed in
Appendix A.3 (printed p.16). It requires the Fourier coefficients to be
pairwise distinct **as complex numbers**. A reflection that is not a shift
can therefore be distinguished. The original Matzinger--Lember theorem
is not silently substituted for this shift-only statement.

Here 0<r<1. The four groups

$$\{1\},\quad\{re^{i\theta},re^{-i\theta}\},\quad
\{r^3e^{i\theta},r^3e^{-i\theta}\},\quad\{r^4\}$$

have distinct moduli 1,r,r^3,r^4. Within either conjugate pair, the two
complex numbers differ exactly when sin(theta)!=0. Thus all six Fourier
coefficients are pairwise distinct as complex numbers in the nonresonant
case; their six absolute values are not pairwise distinct. Applying that
theorem distinguishes the chiral labeling from its reflection. At
sin(theta)=0 the direct symmetry argument applies. The all-length
dichotomy is consequently a known consequence, whereas the explicit
one-pair, length-four formula is the candidate refinement.

Periodic-sampling ambiguity itself is also known; Bauer--Seifert--van der
Meer [3], Section 3.2.2, give different equilibrium/nonequilibrium generators
with one sampled propagator. The general three-word obstruction is [1].
The remaining novelty question is narrowly whether the explicit sharp
four-consecutive-symbol result on this minimal chiral homogeneous ring
has already been proved, or follows immediately from another known formula.
See PRIOR_ART.md for the recovered Matzinger--Lember manuscript and its
version/access limits. The scoped search has not settled historical
novelty. REFERENCES are PARTIAL and NOVELTY is INCONCLUSIVE. An independent
AI proof-review report has been received within the scope above; human peer
review has not been performed. The direct proof in Sections 2-5 does not
depend on FTY. Further source-access details are in PRIOR_COMPARISON.md.

## References

[1] L. Arola-Fernandez and L. Lacasa (2023), *Irreversibility of symbolic
time series: a cautionary tale*. Phys. Rev. E 108, 014201.
https://arxiv.org/pdf/2303.11868
https://doi.org/10.1103/PhysRevE.108.014201

[2] H. Finucane, O. Tamuz and Y. Yaari (2014), *Scenery reconstruction on
finite abelian groups*. Stochastic Processes and their Applications 124,
2754--2770. The source inspected is the author-hosted manuscript dated
30 March 2014, 17 pages: https://tamuz.caltech.edu/papers/scenery.pdf
https://doi.org/10.1016/j.spa.2014.03.012

[3] M. T. Bauer, U. Seifert and J. van der Meer (2025), *Stroboscopic
measurements in Markov networks: exact generator reconstruction vs.
thermodynamic inference*. J. Phys. A 58, 125001.
https://arxiv.org/html/2412.15642v2
https://doi.org/10.1088/1751-8121/adbc52

Copyright (c) 2026 Ryutaro Yonezu. All rights reserved.
