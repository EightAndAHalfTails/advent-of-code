import re
print sum(map(int, re.compile(r"-?\d+").findall(open("input.txt").read())))
