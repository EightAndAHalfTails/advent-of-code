from operator import mul
g=[[int(l.split()[i].rstrip(',')) for i in [2,4,6,8,10]] for l in open("input.txt")]
print max([reduce(mul,t,1) for t in [k[:-1] for k in [[max(m,0) for m in map(sum,zip(*[j for i in [[p]*n for p, n in zip(g,r)] for j in i]))] for r in [(a, b, c, 100-a-b-c) for a in range(101) for b in range(101-a) for c in range(101-a-b)]] if k[-1]==500]])
