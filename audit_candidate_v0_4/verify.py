"""No.39 candidate: exact finite algebra and independent numerical diagnostics.

Python 3.10+ standard library only. No network, external APIs, or simulation.
Usage: python verify.py --output rerun.json
"""
import argparse
from fractions import Fraction as F
from itertools import product
import json
from math import comb, cos, exp, pi, sin, sqrt
from pathlib import Path
import platform
import sys
import time

# Explicitly add this verified package directory, also under Python -I.
# This supports the reviewer's isolated invocation without PYTHONPATH.
sys.path.insert(0, str(Path(__file__).resolve().parent))
import exact_algebra as A


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def exact_checks():
    # Sum over all microscopic paths for each word, coefficient by coefficient.
    actual = A.sub(A.word('0011'), A.word('1100'))
    target = A.scale(A.mul(A.mul(A.mul(A.d, A.power(A.r, 3)), A.s),
                           A.g_poly()), F(-1, 54))
    rem = A.reduce_circle(A.sub(actual, target))
    require(not rem, 'four-word polynomial identity')
    require(A.total(A.K) == A.one, 'transition kernel normalization')
    # At s=0 each Fourier kernel is symmetric under j -> -j.
    for j in range(6):
        diff = A.sub(A.K[j], A.K[-j % 6])
        require(not {e: q for e, q in diff.items() if e[2] == 0},
                'kernel symmetry at s=0')

    # Exact endpoint factorization G(r,1)=(1-r)^2 H(r).
    at_one = {}
    for e, q in A.g_poly().items():
        ee = (e[0], 0, e[2], e[3])
        at_one[ee] = at_one.get(ee, F(0)) + q
    at_one = {e:q for e,q in at_one.items() if q}
    h = A.total([A.one, A.scale(A.r, 2), A.scale(A.power(A.r, 2), 5),
                 A.scale(A.power(A.r, 3), 6),
                 A.scale(A.power(A.r, 4), 3), A.power(A.r, 6)])
    endpoint = A.mul(A.power(A.sub(A.one, A.r), 2), h)
    require(at_one == endpoint, 'G(r,1) factorization')

    # The positivity certificate on 0 <= t=r^2 <= 3/4.
    qcoef = [4, -12, 7, 16, -14, -4, -1]
    bernstein = [sum(F(qcoef[k]) * F(3,4)**k *
                     F(comb(i,k), comb(6,k))
                     for k in range(i+1)) for i in range(7)]
    expected = [F(4), F(5,2), F(101,80), F(5,8),
                F(403,640), F(443,512), F(535,4096)]
    require(bernstein == expected, 'Bernstein coefficient identity')
    require(all(x > 0 for x in bernstein), 'positive Bernstein coefficients')
    # Exact discriminant polynomial from 4(1-t)G_min(r).
    aa = [F(1), F(-2), F(0), F(4), F(1)]
    disc = [F(0)] * 7
    for k, val in enumerate(aa):
        disc[k] += 4*val
        disc[k+1] -= 4*val
    for k, val in [(2,1), (4,2), (6,1)]:
        disc[k] -= val
    require(disc == [F(x) for x in qcoef], 'quadratic minimum polynomial')

    return {'four_word_identity': 'PASS', 'kernel_normalization': 'PASS',
            'resonant_kernel_symmetry': 'PASS', 'endpoint_factorization': 'PASS',
            'quadratic_minimum_identity': 'PASS',
            'positive_Bernstein_coefficients': [str(x) for x in bernstein]}


def canonical_rotation(f):
    return min(f[k:] + f[:k] for k in range(len(f)))


def reflection_centers(f):
    n = len(f)
    return [k for k in range(n) if all(f[i] == f[(k-i) % n] for i in range(n))]


def coloring_checks():
    result = {}
    for n in (3,4,5,6):
        chiral = []
        necklace_reps = set()
        for f in product((0,1), repeat=n):
            necklace_reps.add(canonical_rotation(f))
            if not reflection_centers(f):
                chiral.append(f)
        expected = 12 if n == 6 else 0
        require(len(chiral) == expected, 'chiral labeling count')
        if n == 6:
            reps = sorted(set(canonical_rotation(f) for f in chiral))
            require(reps == [(0,0,1,0,1,1), (0,0,1,1,0,1)], 'chiral orbit pair')
        result[str(n)] = {'labelings': 2**n, 'rotation_classes': len(necklace_reps),
                          'chiral_labelings': len(chiral),
                          'achiral_labelings': 2**n-len(chiral),
                          'chiral_rotation_representatives': sorted({
                              ''.join(map(str,canonical_rotation(f))) for f in chiral})}
    return result


def kernel_fourier(a,b,t):
    # Independent formula for Fourier inversion, rather than the expanded
    # expressions used in exact_algebra.py.
    s0 = a+b
    return [sum(exp(s0*t*(cos(2*pi*k/6)-1))*
                cos((a-b)*t*sin(2*pi*k/6)-2*pi*k*j/6)
                for k in range(6))/6 for j in range(6)]


def kernel_uniformization(a,b,t):
    # Sum over a Poisson number of nearest-neighbor jumps. The cutoff is
    # deliberately oversized for the fixed diagnostic inputs below.
    mu = (a+b)*t
    require(mu < 100, 'diagnostic range for Poisson expansion')
    v = [1.] + [0.]*5
    w = exp(-mu)
    out = [0.]*6
    for k in range(500):
        for j in range(6):
            out[j] += w*v[j]
        v = [(a*v[(j-1)%6]+b*v[(j+1)%6])/(a+b) for j in range(6)]
        w *= mu/(k+1)
    require(abs(sum(out)-1.) < 2e-13, 'Poisson expansion normalization')
    return out


def word_probability(word, kernel, labels=(0,0,1,0,1,1)):
    n = len(labels)
    v = [float(y == int(word[0]))/n for y in labels]
    for bit in word[1:]:
        v = [sum(v[i]*kernel[(j-i) % n] for i in range(n)) *
             int(labels[j] == int(bit)) for j in range(n)]
    return sum(v)


def closed_difference(a,b,t):
    r = exp(-(a+b)*t/2)
    theta = sqrt(3)*(a-b)*t/2
    c = cos(theta)
    g = 1-2*r*r+4*r**6+r**8+4*r*r*(1-r*r)*c*c-2*r**3*(1+r**4)*c
    return -sqrt(3)/54*r**3*sin(theta)*g


def numerical_checks():
    # Numerical results support implementation only, never decide exact zero.
    rates = [(2.,1.), (1.,2.), (4.,.25), (.25,4.), (1.5,.5),
             (.5,1.5), (1.,1.), (.7,2.)]
    times = [.01,.03,.1,.2,.4,.7,1.,1.3,1.8,2.5]
    max_kernel = max_delta = max_short = 0.
    max_symmetry = max_resonant = 0.
    count = 0
    rows = []
    for a,b in rates:
        for t in times:
            ku = kernel_uniformization(a,b,t)
            kf = kernel_fourier(a,b,t)
            max_kernel = max(max_kernel, max(abs(x-y) for x,y in zip(ku,kf)))
            delta = word_probability('0011',ku)-word_probability('1100',ku)
            formula = closed_difference(a,b,t)
            max_delta = max(max_delta,abs(delta-formula))
            for length in (1,2,3):
                for w in product('01',repeat=length):
                    w = ''.join(w)
                    max_short = max(max_short,abs(word_probability(w,ku)-
                                                 word_probability(w[::-1],ku)))
            count += 1
            if (a,b,t) in [(2.,1.,.1),(2.,1.,.7),(4.,.25,.4)]:
                rows.append({'a':a,'b':b,'tau':t,'difference_uniformization':delta,
                             'difference_closed_formula':formula})
    # Check four-word reversal on all achiral labelings at several inputs.
    achiral_checks = 0
    for labels in product((0,1),repeat=6):
        if not reflection_centers(labels):
            continue
        for a,b,t in [(2.,1.,.1),(2.,1.,.7),(1.,2.,.4)]:
            ku = kernel_uniformization(a,b,t)
            for w in product('01', repeat=4):
                w = ''.join(w)
                err = abs(word_probability(w,ku,labels)-
                          word_probability(w[::-1],ku,labels))
                max_symmetry = max(max_symmetry,err)
                achiral_checks += 1
    resonant_checks = 0
    for a,b in [(2.,1.),(1.,2.),(4.,.25),(.25,4.)]:
        for m in (1,2,3):
            t = 2*pi*m/(sqrt(3)*abs(a-b))
            ku = kernel_uniformization(a,b,t)
            require(max(abs(ku[j]-ku[-j%6]) for j in range(6)) < 2e-13,
                    'resonant kernel symmetry diagnostic')
            for length in range(1,7):
                for w in product('01',repeat=length):
                    w = ''.join(w)
                    max_resonant = max(max_resonant,abs(word_probability(w,ku)-
                                                       word_probability(w[::-1],ku)))
                    resonant_checks += 1
    require(max(max_kernel,max_delta,max_short,max_symmetry,max_resonant) < 2e-13,
            'floating point diagnostic tolerance')
    return {'rate_time_cases':count, 'max_kernel_difference':max_kernel,
            'max_word_difference_error':max_delta, 'max_short_word_asymmetry':max_short,
            'achiral_four_word_pairs':achiral_checks,
            'max_achiral_word_asymmetry':max_symmetry,
            'resonant_word_pairs':resonant_checks,
            'max_resonant_word_asymmetry':max_resonant,
            'illustrations':rows,
            'limits':'binary64 diagnostics; no interval bounds; small values are not declared zero'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output',type=Path)
    args = parser.parse_args()
    started = time.perf_counter()
    result = {'candidate':'No.39 v0.2', 'date':'2026-10-25',
              'python':sys.version, 'platform':platform.platform(),
              'exact_algebra':exact_checks(), 'colorings':coloring_checks(),
              'numerical_diagnostics':numerical_checks(),
              'external_proof_audit':'NOT_RUN', 'external_numerical_review':'SUPPLIED_REPORT_PASS_NOT_RERUN_HERE', 'novelty':'INCONCLUSIVE'}
    result['elapsed_seconds'] = time.perf_counter()-started
    data = json.dumps(result,indent=2,ensure_ascii=False)+'\n'
    if args.output:
        args.output.write_text(data,encoding='utf-8')
    print('PASS exact polynomial identity and positivity certificates')
    print('PASS exhaustive binary colorings on cycles of lengths 3,4,5,6')
    print('PASS independent uniformization/Fourier diagnostics')
    print('NOVELTY INCONCLUSIVE / EXTERNAL PROOF AUDIT NOT RUN')
    if args.output:
        print(args.output)


if __name__ == '__main__':
    main()
