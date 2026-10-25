"""Separate exact positivity audit: dense univariate rational arithmetic.

Does not import verify.py or exact_algebra.py. Reconstructs the Bernstein
polynomial by expanding the proposed basis functions in the reverse direction.
This is an internal additional check, not an external mathematical review.
"""
import argparse
from fractions import Fraction as F
import json
from math import comb
from pathlib import Path
import sys


def trim(p):
    p = list(map(F,p))
    while len(p)>1 and not p[-1]:
        p.pop()
    return p


def plus(p,q):
    z = [F(0)] * max(len(p),len(q))
    for i,a in enumerate(p): z[i] += a
    for i,a in enumerate(q): z[i] += a
    return trim(z)


def times(p,q):
    z = [F(0)] * (len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q): z[i+j] += a*b
    return trim(z)


def multiple(p,k):
    return trim([k*x for x in p])


def power(p,n):
    ans = [F(1)]
    for _ in range(n): ans = times(ans,p)
    return ans


def check(condition,message):
    if not condition: raise AssertionError(message)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output',type=Path)
    args = parser.parse_args()
    B = [F(4),F(5,2),F(101,80),F(5,8),F(403,640),F(443,512),F(535,4096)]
    basis = [times([F(0)]*j+[F(comb(6,j))],power([1,-1],6-j))
             for j in range(7)]
    expansion = [F(0)]
    partition = [F(0)]
    for b,p in zip(B,basis):
        expansion = plus(expansion,multiple(p,b))
        partition = plus(partition,p)
    q = [F(x) for x in [4,-12,7,16,-14,-4,-1]]
    expected = [a*F(3,4)**j for j,a in enumerate(q)]
    check(expansion == expected,'direct Bernstein expansion')
    check(partition == [F(1)],'Bernstein partition of unity')
    check(all(b>0 for b in B),'strictly positive Bernstein coefficients')

    # G=A*c^2+B*c+C and the polynomial from completing the square.
    A = [F(0),F(0),F(4),F(0),F(-4)]
    lin = [F(0),F(0),F(0),F(-2),F(0),F(0),F(0),F(-2)]
    C = [F(1),F(0),F(-2),F(0),F(0),F(0),F(4),F(0),F(1)]
    q_r2 = [F(0)]*13
    for j,a in enumerate(q): q_r2[2*j] = a
    # 4*A*C-lin^2 = 4*r^2*q(r^2).
    discriminant = plus(multiple(times(A,C),4),multiple(times(lin,lin),-1))
    check(discriminant == trim([0,0]+[4*a for a in q_r2]),
          'completed-square identity')

    G_at_c1 = plus(plus(A,lin),C)
    H = [1,2,5,6,3,0,1]
    check(G_at_c1 == times(power([1,-1],2),H),'endpoint factorization')

    # L(r)=r+r^5-4+4r^2; its derivative is positive for r>0.
    L = [-4,1,4,0,0,1]
    derivative = [F(j)*F(L[j]) for j in range(1,len(L))]
    check(derivative == list(map(F,[1,8,0,0,5])),'threshold derivative')
    # L(sqrt(3)/2)=25*sqrt(3)/32-1 > 0, by squaring positive terms.
    threshold_square_margin = F(25,32)**2*3-1
    check(threshold_square_margin>0,'exact threshold sign')
    check(sum(G_at_c1)==0,'strict-positivity endpoint excludes r=1,c=1')

    report = {
        'status':'PASS', 'scope':'additional internal exact positivity audit',
        'imports_original_verifiers':False, 'python':sys.version,
        'method':'expand rational Bernstein basis into ordinary coefficients',
        'checks':{
            'Bernstein_expansion':True,'partition_of_unity':True,
            'positive_Bernstein_coefficients':True,'completed_square':True,
            'endpoint_factorization':True,'threshold_derivative':True,
            'threshold_positive_by_exact_square':True,
            'excluded_endpoint_G_1_1_is_zero':True},
        'B':[str(b) for b in B],
        'q_3u_over4_power_coefficients':[str(a) for a in expansion],
        'threshold_square_margin':str(threshold_square_margin),
        'review_limit':'not an independent external proof audit'}
    if args.output:
        args.output.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print('PASS: separate dense-rational Bernstein and case-split audit')
    if args.output: print(args.output)


if __name__=='__main__': main()
