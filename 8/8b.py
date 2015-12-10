print sum([2+L.count('"')+L.count('\\') for L in open("input.txt")])
