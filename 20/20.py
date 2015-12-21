def p(n):
    return 10*sum(set((i+n/i if i!=n/i else i) for i in range(1,int(n**0.5+1))if n%i==0))
def q(n):
    return 11*sum(set((i if n/i<=50 else 0)+(n/i if i<=50 and i!=n/i else 0) for i in range(1,int(n**0.5+1))if n%i==0))
h=1
while True:
    if p(h)>=29000000:
        print 'a',h
    if q(h)>=29000000:
        print 'b',h
        break
    h+=1
