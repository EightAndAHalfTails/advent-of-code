from itertools import *
W = {}
for L in open("input.txt"):
    L = L.split()
    try:
        W[L[0]][L[2]] = int(L[-1])
    except KeyError:
        W[L[0]] = {}
        W[L[0]][L[2]] = int(L[-1])
    try:
        W[L[2]][L[0]] = int(L[-1])
    except KeyError:
        W[L[2]] = {}
        W[L[2]][L[0]] = int(L[-1])
print min([sum([W[t][f] for t, f in zip(c[:-1], c[1:])]) for c in permutations(W.keys())])
print max([sum([W[t][f] for t, f in zip(c[:-1], c[1:])]) for c in permutations(W.keys())])
        
                
