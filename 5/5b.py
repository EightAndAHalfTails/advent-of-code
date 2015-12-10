print [True in [y in x or y in z for x,y,z in [(L[:i],L[i:i+2],L[i+2:]) for i in range(len(L)-2)]] and True in [a==c for a,b,c in zip(L,L[1:],L[2:])] for L in open("input.txt")].count(True)
