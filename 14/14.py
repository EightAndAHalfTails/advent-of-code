print max([(v*t*(2503/(t+r))+v*min(t, 2503%(t+r)))for v, t, r in[(int(l.split()[3]), int(l.split()[6]), int(l.split()[-2]))for l in open("input.txt")]])
print max(map(sum,zip(*[[int(i==max(s))for i in s]for s in zip(*[[(v*t*(x/(t+r))+v*min(t,x%(t+r)))for x in range(1,2504)]for v,t,r in[(int(l.split()[3]),int(l.split()[6]),int(l.split()[-2]))for l in open("input.txt")]])])))
