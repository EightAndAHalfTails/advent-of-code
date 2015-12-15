import itertools
s={}
with open("input.txt") as f:
    for l in f:
        w=l.split()
        n=int(w[3])
        if w[2]=="lose":
            n=-n
        try:
            s[w[0]][w[-1].rstrip('.')]=n
        except KeyError:
            s[w[0]]={}
            s[w[0]][w[-1].rstrip('.')]=n
print max([sum([s[p[0]][p[1]] + s[p[1]][p[0]] for p in zip(a,a[1:]+(a[0],))]) for a in itertools.permutations(s.keys())])
print max([max([sum([s[p[0]][p[1]] + s[p[1]][p[0]] for p in zip(a,a[1:]+(a[0],))]) - (s[r[0]][r[1]] + s[r[1]][r[0]]) for r in zip(a,a[1:]+(a[0],))]) for a in itertools.permutations(s.keys())])
