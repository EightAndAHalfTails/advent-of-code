p = 0
r = 0
with open("input.txt") as f:
    for line in f:
        (l, w, h) = map(int, line.split('x'))
        p+=2*l*w+2*w*h+2*h*l+min(l*w, w*h, h*l)
        r+=min(2*(l+w), 2*(w+h), 2*(h+l))+l*w*h
print p
print r
