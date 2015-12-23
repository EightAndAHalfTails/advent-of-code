m=(53,73,113,173,229)
def t(w,b,e,c,tc,l):
    #print "player turn",tc,":",w,b,e,c
    #if(w[0]<b[0]/3):
    #    print "no chance"
    #    return float('inf')
    y=w[0]-1
    if y<1:
        #print "died of dysentery",l
        return float('inf')
    
    s=max(0,e[0]-1)
    x=b[0]-3*int(e[1]>0)
    p=max(0,e[1]-1)
    z=w[1]-m[c]+101*int(e[2]>0)
    r=max(0,e[2]-1)

    if x<1:
        print "boss died",l+[c],sum([m[i] for i in l+[c]])
        return m[c]
    
    if c==0:
        x-=4
    if c==1:
        y+=2
        x-=2
    if c==2:
        s=6
    if c==3:
        p=6
    if c==4:
        r=5

    if x<1:
        print "player defeated boss",l+[c],sum([m[i] for i in l+[c]])
        return m[c]

    #print "boss   turn",tc+1,":",(y,z),(x,b[1]),(s,p,r)
    a=7*int(s>0)
    s=max(0,s-1)
    x=x-3*int(p>0)
    p=max(0,p-1)
    z=z+101*int(r>0)
    r=max(0,r-1)

    if x<1:
        print "boss died",l+[c],sum([m[i] for i in l+[c]])
        return m[c]

    y-=(b[1]-a)
    if y<1:
        #print "player loses",l
        return float('inf')

    try:
        return m[c]+min([t((y,z),(x,b[1]),(s,p,r),n,tc+2,l+[c]) for n in range(5) if (m[n]<=z+101*int(e[2]>0) and not(n>1 and (s,p,r)[n-2]>1))])
    except ValueError:
        #print "out of mana",l
        return float('inf')
print min([t((50,500),(71,10),(0,0,0),n,0,[]) for n in range(5)])
