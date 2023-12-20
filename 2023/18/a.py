lines = list(map(lambda x: x.strip(), open('input', 'r').readlines()))
edging = set()
x = y = 0
DIRECTIONS = {
    'L': [-1, 0],
    'R': [1, 0],
    'U': [0, -1],
    'D': [0, 1]
}
for i in range(len(lines)):
    heading, count, color = lines[i].split()
    dx, dy = DIRECTIONS[heading]
    for j in range(int(count)):
        x += dx
        y += dy
        edging.add((x,y))

topleft = min(edging, key=lambda x: (x[1],x[0]))
bottomright = max()
