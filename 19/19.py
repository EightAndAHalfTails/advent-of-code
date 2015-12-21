import re
r=[]
s=''
with open("input.txt") as f:
    for l in f:
        try:
            r+=[(l.split()[0],l.split()[2])]
        except IndexError:
            s=l.rstrip('\n')
print len(set.union(*[set([s[:i]+s[i:].replace(f,t,1)for i in[m.start()for m in re.finditer(f,s)]])for f,t in r]))
