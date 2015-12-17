x=[int(l)for l in open("input.txt")]
def e(c,t):
    if t==0:
        return 1
    elif len(c)==1:
        return int(c[0]==t)
    else:
        return sum([e(c[i+1:],t-c[i])for i in range(len(c))if t-c[i]>=0])
print e(x,150)
