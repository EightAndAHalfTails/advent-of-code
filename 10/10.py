from itertools import *
def i(s):
     return "".join([str(len(l))+l[0] for l in [list(g) for k, g in groupby(s)]])
x = "1113222113"
for _ in range(50):
    x = i(x)
print len(x)
