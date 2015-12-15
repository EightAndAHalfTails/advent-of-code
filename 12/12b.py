from json import load
def e(a):
    try:
        if "red" in a.values():
            return 0
        else:
            return sum(e(n) for n in a.values())
    except AttributeError:
        if type(a) is list:
            return sum(e(n) for n in a)
        elif type(a) is int:
            return a
    return 0
print e(load(open("input.txt")))
    
