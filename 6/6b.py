from collections import Counter
l=Counter()
for L in open("input.txt"):
    s = L.split()
    x, y = map(int, s[-1].split(','))
    a, b = map(int, s[-3].split(','))
    n = Counter([v+1000*w for v in range(a, x+1) for w in range(b,y+1)])
    if s[:-3] == ["turn", "on"]:
        l += n
    if s[:-3] == ["toggle"]:
        l += n+n
    if s[:-3] == ["turn", "off"]:
        l -= n
print sum(l.values())
