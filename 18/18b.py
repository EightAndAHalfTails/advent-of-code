g=[[0]*102] + [[0] + [int(c=='#')for c in l] for l in open("input.txt")] + [[0]*102]
for r in [1,100]:
    for c in [1,100]:
        g[r][c]=1
def i(x):
    y=[[0 for _ in range(102)] for _ in range(102)]
    for r in range(1,101):
        for c in range(1,101):
            n=sum([x[a][b] for a in [r-1,r,r+1] for b in [c-1,c,c+1]])
            y[r][c] = int(2<n<5) if x[r][c] else int(n==3)
    return y
for t in range(100):
    g=i(g)
    for r in [1,100]:
        for c in [1,100]:
            g[r][c]=1
print sum([l.count(1) for l in g])
