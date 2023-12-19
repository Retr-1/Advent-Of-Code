lines = list(map(lambda x: x.strip(), open('input', 'r').readlines()))
total = 0
h = len(lines)
for x in range(len(lines[0])):
    i = 0
    for y in range(len(lines)):
        if lines[y][x] == 'O':
            total += h-i
            i += 1
        elif lines[y][x] == '#':
            i = y+1
print(total)