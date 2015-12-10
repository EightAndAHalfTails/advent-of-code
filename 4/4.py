import hashlib
s="ckczppom"
i=0
v=False
x=False
while (v,x) != (True,True):
    if ~v&(hashlib.md5(s+str(i)).hexdigest()[0:5]=="00000"):
        print i
        v=True
    if ~x&(hashlib.md5(s+str(i)).hexdigest()[0:6]=="000000"):
        print i
        x=True
    i+=1
