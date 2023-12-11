lines = list(map(lambda x: x.strip(), open('input', 'r').readlines()))
WIDTH = len(lines[0])
HEIGHT = len(lines)

for y in range(HEIGHT-1, -1, -1):
    for x in range(WIDTH):
        if lines[y][x] != '.':
            break
    else:
        lines.insert(y, '.'*WIDTH)
HEIGHT = len(lines)

for x in range(WIDTH-1, -1, -1):
    for y in range(HEIGHT):
        if lines[y][x] != '.':
            break
    else:
        for y in range(HEIGHT):
            lines[y] = lines[y][:x] + '.' + lines[y][x:]
WIDTH = len(lines[0])

galaxies = []
for x in range(WIDTH):
    for y in range(HEIGHT):
        if lines[y][x] == '#':
            galaxies.append((x,y))

total = 0
for i in range(len(galaxies)):
    for j in range(i+1, len(galaxies)):
        x1,y1 = galaxies[i]
        x2,y2 = galaxies[j]
        total += abs(x1-x2) + abs(y1-y2)

print(total)

