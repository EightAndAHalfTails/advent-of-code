from operator import mul
from itertools import combinations

x=[1,2,3,4,5,7,8,9,10,11]
x=[int(l) for l in open("input.txt")]

def g(x,s):
    a=[]
    for n in xrange(1,len(x)+1):
        a=[r for r in combinations(x,n) if sum(r)==s]
        if a!=[]:
            return a
    return []
print min([reduce(mul,a,1)for a in g(x,sum(x)/3)if g([c for c in x if c not in a],sum(x)/3) != []])
print min([reduce(mul,a,1)for b in g([c for c in x if c not in a],sum(x)/4)for a in g(x,sum(x)/4)if g([c for c in x if c not in a and c not in b],sum(x)/4)!=[]])
            
