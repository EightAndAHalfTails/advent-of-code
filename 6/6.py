l=set()
for L in open("input.txt"):
    s = L.split()
    x, y = map(int, s[-1].split(','))
    a, b = map(int, s[-3].split(','))
    n = [(v, w) for v in range(a, x+1) for w in range(b,y+1)]
    if s[:-3] == ["turn", "on"]:
        l = l.union(n)
    if s[:-3] == ["toggle"]:
        l = l.union(n) - l.intersection(n)
    if s[:-3] == ["turn", "off"]:
        l = l - set(n)
print len(l)
