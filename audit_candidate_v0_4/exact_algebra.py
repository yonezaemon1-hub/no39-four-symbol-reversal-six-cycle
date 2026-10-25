"""Exact finite polynomial algebra for the No.39 candidate; standard library only."""
from fractions import Fraction as F
from itertools import product

# variables r,c,s,d with d**2=3; d represents sqrt(3)
ZERO=(0,0,0,0)
def const(q): return {ZERO:F(q)} if q else {}
def var(i):
    e=[0]*4; e[i]=1
    return {tuple(e):F(1)}
def add(a,b):
    z=a.copy()
    for e,q in b.items(): z[e]=z.get(e,0)+q
    return {e:q for e,q in z.items() if q}
def scale(a,q): return {e:v*q for e,v in a.items() if v*q}
def sub(a,b): return add(a,scale(b,-1))
def mul(a,b):
    z={}
    for e,q in a.items():
      for f,v in b.items():
        g=tuple(x+y for x,y in zip(e,f))
        d=g[3]; g=g[:3]+(d%2,)
        z[g]=z.get(g,0)+q*v*3**(d//2)
    return {e:q for e,q in z.items() if q}
def power(a,n):
    z=const(1)
    for _ in range(n):z=mul(z,a)
    return z
def total(terms):
    z={}
    for t in terms:z=add(z,t)
    return z
def show(a):
    return ' + '.join(f'{q}*'+''.join(f'{v}^{n}' for v,n in zip('rcsd',e) if n) for e,q in sorted(a.items())) or '0'
r,c,s,d=[var(i) for i in range(4)]
r3=power(r,3); r4=power(r,4)
one=const(1)
rc=mul(r,c); rs=mul(r,s); r3c=mul(r3,c); r3s=mul(r3,s)
drs=mul(d,rs); dr3s=mul(d,r3s)
K=[
 total([one,r4,scale(rc,2),scale(r3c,2)]),
 total([one,scale(r4,-1),rc,drs,scale(r3c,-1),dr3s]),
 total([one,r4,scale(rc,-1),drs,scale(r3c,-1),scale(dr3s,-1)]),
 total([one,scale(r4,-1),scale(rc,-2),scale(r3c,2)]),
 total([one,r4,scale(rc,-1),scale(drs,-1),scale(r3c,-1),dr3s]),
 total([one,scale(r4,-1),rc,scale(drs,-1),scale(r3c,-1),scale(dr3s,-1)])]
K=[scale(k,F(1,6)) for k in K]
labels=[0,0,1,0,1,1]
def word(w,labels=labels):
    a={}
    for states in product(*[[i for i,y in enumerate(labels) if y==int(b)] for b in w]):
        v=const(F(1,6))
        for i,j in zip(states,states[1:]):v=mul(v,K[(j-i)%6])
        a=add(a,v)
    return a
def reduce_circle(a):
    """Canonical remainder using c**2=1-s**2."""
    out={}
    for e,q in a.items():
        rem={e[:1]+(e[1]%2,)+e[2:]:q}
        out=add(out,mul(rem,power(sub(one,power(s,2)),e[1]//2)))
    return out

def g_poly():
    return total([one,scale(power(r,2),-2),scale(power(r,6),4),power(r,8),
        scale(mul(mul(power(r,2),sub(one,power(r,2))),power(c,2)),4),
        scale(mul(mul(power(r,3),add(one,power(r,4))),c),-2)])

if __name__=='__main__':
    a=sub(word('0011'),word('1100'))
    print('p0011-p1100 =',show(a))
    print('circle reduced =',show(reduce_circle(a)))
    print('normalization =',show(total(K)))
