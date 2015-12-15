from string import *
from itertools import *
a=ascii_lowercase
def v(p):
    return True in [x+y+z in a for (x,y,z) in zip(p[:-2],p[1:-1],p[2:])] and True not in [c in p for c in "iol"] and sum([l for l in [len(list(g)) for k, g in groupby(p)] if l>1])>3
def n(p):
    p=list(p)
    c=0
    i=-1
    while True:
        p[i] = (a[1:]+'a')[a.index(p[i])]
        if p[i] == 'a': i-=1
        else: break
    return ''.join(p)
p="cqjxjnds"
p="cqjxxyzz"
p=n(p)
while not v(p):
    p=n(p)
print p

