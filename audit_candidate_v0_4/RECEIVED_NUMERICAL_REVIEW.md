# Received numerical review report — 25 October 2026

Source: the report supplied by the user in this conversation. The reviewer
described the work as an independent numerical check. Reviewer identity,
code, random seed, sampled parameter points, and raw outputs were not supplied.
The 3,000-point SciPy experiment was **not rerun by this package's author**.

## Reported results

| Check | Reported outcome |
| --- | --- |
| Original check_hashes.py | PASS for 8 files |
| Original verify.py | PASS |
| Separate scipy.linalg.expm implementation, 3,000 random (a,b,tau) points | Formula maximum discrepancy 1.1e-16 |
| Grid evaluation of G(r,c) | Minimum approximately 1.8e-7 near the r=1 boundary; no negative value found |
| Reversal differences for word lengths 2 and 3 | Approximately 3e-17 |
| Resonant-spacing row | The supplied Markdown table row was truncated; no missing result has been reconstructed |

The reviewer explicitly limited these results to finite numerical evaluation
and did not claim an independent derivation of the proof. The reviewer did
not audit novelty and requested a separate look at the Bernstein certificate,
the case split at r^2=3/4, and Matzinger--Lember (2006).

The review correctly emphasizes that G>0 is asserted on 0<r<1, and that the
word-length result concerns stationary, equally spaced observations on the
homogeneous ring with fixed labels. It does not concern deciding from one
four-bit sample.

The report also noted that Python -I prevents the original bare local-module
import in verify.py. Ordinary invocation passed. v0.2 adds the package's own
directory explicitly, and records a successful -I execution. This is an
execution convenience change; no mathematical algorithm is changed.

## Status interpretation

External numerical review: **reported PASS**.

External independent mathematical proof audit: **not supplied**.

Historical novelty audit by that reviewer: **not performed**.

No human journal/conference peer review is claimed.
