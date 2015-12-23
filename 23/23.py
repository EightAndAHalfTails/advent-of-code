p=[l.rstrip('\n')for l in open("input.txt")]
for r in [[0,0],[1,0]]:
    c=0
    while True:
        try:
            o=p[c].split()
        except IndexError:
            break
        r[int(o[1][0]=="b")] = r[int(o[1]=="b")]/2 if o[0]=="hlf" else 3*r[int(o[1]=="b")]if o[0]=="tpl" else 1+r[int(o[1]=="b")]if o[0]=="inc" else r[int(o[1][0]=="b")]
        c+=int(o[1]) if o[0]=="jmp" else int(o[2])if (o[0]=="jie" and int(r[int(o[1]=="b,")]%2==0)or o[0]=="jio" and int(r[int(o[1]=="b,")]==1))else 1
    print r[1]
