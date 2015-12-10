floor = 0
pos = 0
with open("input.txt") as f:
    for line in f:
        for char in line:
            pos += 1
            floor += 1 if char == "(" else -1
            if floor == -1:
                print pos
print floor
