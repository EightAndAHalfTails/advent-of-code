d = {}
for L in open("input.txt"):
    p = L.rstrip('\n').split(" -> ")
    d[p[1]] = p[0]
d["b"] = 956
def e(x):
    if type(x) is int:
        return x
    try:
        d[x] = int(x)
        return d[x]
    except ValueError:
        pass
    if type(d[x]) is int:
        return d[x]
    o = d[x].split()
    if len(o) == 1:
        d[x] = e(o[0])
    elif len(o) == 2:
        d[x] = ~e(o[1])
    elif o[1][1:] == "SHIFT":
        d[x] = e(o[0]) << int(o[2]) if o[1][0] == "L" else e(o[0]) >> int(o[2])
    elif o[1] == "AND":
        d[x] =  e(o[0]) & e(o[2])
    elif o[1] == "OR":
        d[x] = e(o[0]) | e(o[2])
    else:
        return ValueError
    return d[x]
print e("a")
