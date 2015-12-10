import operator, itertools
c={'v':(0,-1),'>':(1,0),'<':(-1,0),'^':(0,1)}
s=set()
p=(0,0)
r=(0,0)
s.add(p)
def g(x):
    a = iter(x)
    return itertools.izip(a, a)
with open("input.txt") as f:
    for line in f:
        for a, b in g(line):
            p=tuple(map(operator.add,p,c[a]))
            r=tuple(map(operator.add,r,c[b]))
            s.add(p)
            s.add(r)
print len(s)
