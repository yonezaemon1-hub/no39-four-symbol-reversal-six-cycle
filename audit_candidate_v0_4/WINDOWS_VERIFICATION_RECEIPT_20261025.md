# No.39 Windows verification receipt — 25 October 2026

**Result: PASS from the user-supplied Windows execution log for v0.2.**

| Item | Received evidence |
| --- | --- |
| Python | 3.12.10 |
| Shell / environment | Windows PowerShell output; detailed OS build not printed |
| Tested package | No39_candidate_v0_2 |
| Original file manifest | 15 files PASS |
| Exact polynomial identity and positivity certificates | PASS |
| Exhaustive binary colorings, cycle lengths 3,4,5,6 | PASS |
| Uniformization/Fourier diagnostics | PASS |
| Separate dense-rational positivity audit | PASS |
| Main output filename | rerun_win.json |
| Positivity output filename | positivity_win.json |

## Received SHA256

The user's PowerShell output reports this SHA256 for `rerun_win.json`:

```text
24ACC41FB3D40569A40EF07D0C2F414915D4C59DBD553705345335DD48A2F368
```

This is a recorded user-displayed hash. The JSON file itself was not attached,
so its bytes, contents and SHA256 have not been independently inspected here.
No hash for positivity_win.json was supplied.

## Applicability to v0.3

The four Python programs below were compared byte for byte between the local
v0.2 and v0.3 packages and are identical:

| Program | SHA256 of both copies |
| --- | --- |
| verify.py | 45351245194c0efd87a9bb5084d75a0ef8834ee26f4b1bfc97a6a94f97520b78 |
| exact_algebra.py | 7a3895557a01453328fc9c9c2b0f43b8762b3888bc9955c0ebe56235085e6e4c |
| audit_positivity_dense.py | ed921aa47c9276ea5777e7b4c273674bbbbab674733080e7e8f64580d01e7324 |
| check_hashes.py | a9439e69d2e9efaa0130f39938bf19cd40f3cc60193df00c511abab13a5585f7 |

The Windows execution therefore supplies runtime-reproduction evidence for
the same mathematical verification implementation included in v0.3. The
15-file manifest run is specifically a v0.2 package-integrity check; it is
not relabeled as a Windows check of the expanded v0.3 document manifest.

The former Windows-runtime verification gap is closed at this logged scope.
An independent external proof audit and historical novelty are separate
questions. Their status is not changed by this run.

## Execution log supplied by the user

The initial fragment of the submitted command was truncated. The following
complete output lines are retained without reconstructing that command:

```text
PASS CHANGES.json
PASS FOLLOWUP_AUDIT.md
PASS LICENSE.txt
PASS PRIOR_ART.md
PASS PROOF.md
PASS README.md
PASS RECEIVED_NUMERICAL_REVIEW.md
PASS audit_positivity_dense.py
PASS check_hashes.py
PASS evidence.json
PASS evidence_v0_2.json
PASS exact_algebra.py
PASS history/original_v0_1.zip
PASS positivity_dense_evidence.json
PASS verify.py
PASS 15 files
PASS exact polynomial identity and positivity certificates
PASS exhaustive binary colorings on cycles of lengths 3,4,5,6
PASS independent uniformization/Fourier diagnostics
NOVELTY INCONCLUSIVE / EXTERNAL PROOF AUDIT NOT RUN
rerun_win.json
PASS: separate dense-rational Bernstein and case-split audit
positivity_win.json
Python 3.12.10
Path
----
C:\Users\meteo\No39_test\No39_candidate_v0_2

Algorithm : SHA256
Hash      : 24ACC41FB3D40569A40EF07D0C2F414915D4C59DBD553705345335DD48A2F368
Path      : C:\Users\meteo\No39_test\No39_candidate_v0_2\rerun_win.json
```
