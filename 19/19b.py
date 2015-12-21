import re
r=[]
s=''
with open("input.txt") as f:
    for l in f:
        try:
            r+=[(l.split()[0],l.split()[2])]
        except IndexError:
            s=l.rstrip('\n')
b=float('inf')
z=set()
def e(x,d=0):
    global b
    if x in z:
        return b
    z.add(x)
    if d>=b:
        return b
    if x=='e':
        b=d
        print d
        return d
    try:
        print x,d
        return min([e(y,d+1) for y in set.union(*[set([x[:i]+x[i:].replace(t,f,1)for i in[m.start()for m in re.finditer(t,x)]])for f,t in r])])
    except ValueError:
        return b
print e(s)
