x=[int(l)for l in open("input.txt")]
def e(c,t,m,d=0):
    if d==m:
        return 0
    if t==0:
        return 1
    elif len(c)==1:
        return int(c[0]==t)
    else:
        return sum([e(c[i+1:],t-c[i],m,d+1)for i in range(len(c))if t-c[i]>=0])
m=1
while True:
    n=e(x,150,m)
    if n>0:
        print n
        break
    m+=1
