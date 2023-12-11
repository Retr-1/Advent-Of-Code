lines = list(map(lambda x: x.strip(), open('input', 'r').readlines()))
WIDTH = len(lines[0])
HEIGHT = len(lines)
EXPAND = 10**6-1

add_vertical = [0]*HEIGHT
add_horizontal = [0]*WIDTH

for y in range(HEIGHT):
    for x in range(WIDTH):
        if lines[y][x] != '.':
            break
    else:
        add_vertical[y] += EXPAND
    add_vertical[y] += add_vertical[y-1]
    
for x in range(WIDTH):
    for y in range(HEIGHT):
        if lines[y][x] != '.':
            break
    else:
        add_horizontal[x] += EXPAND
    add_horizontal[x] += add_horizontal[x-1]


galaxies = []
for x in range(WIDTH):
    for y in range(HEIGHT):
        if lines[y][x] == '#':
            galaxies.append((x+add_horizontal[x],y+add_vertical[y]))

total = 0
for i in range(len(galaxies)):
    for j in range(i+1, len(galaxies)):
        x1,y1 = galaxies[i]
        x2,y2 = galaxies[j]
        total += abs(x1-x2) + abs(y1-y2)

print(total)

