t=(2981,3075)
c=20151125
z=3
while True:
    for x,y in zip(xrange(1,z),xrange(z-1,0,-1)):
        c=c*252533%33554393
        if (y,x)==t:
            print c
            exit(0)
    z+=1
