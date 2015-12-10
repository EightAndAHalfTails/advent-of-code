n=0
with open("input.txt") as f:
    for L in f:
        if sum([L.count(c) for c in "aeiou"])<3:
            continue
        d=True
        for i in range(len(L)-1):
            if L[i]==L[i+1]:
                d=False
        if d:
            continue
        if True in [L.count(s)>0 for s in ["ab", "cd", "pq", "xy"]]:
            continue
        n+=1
print n
