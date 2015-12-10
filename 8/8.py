n=0
for L in open("input.txt"):
    i=0
    while L[i] != '\n':
        if L[i] == '"':
            n+=1
        try:
            if L[i:i+2] == '\\\\' or L[i:i+2] == '\\"':
                n+=1
                i+=1
            elif L[i:i+2] == '\\x':
                n+=3
                i+=1
        except IndexError:
            pass
        i+=1
print n
