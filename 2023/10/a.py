lines = list(map(lambda x: x.strip(), open('input', 'r').readlines()))

for y, line in enumerate(lines):
    if (x:=line.find('S')) != -1:
        start = (x,y)

NORTH,WEST,SOUTH,EAST = range(4)
PIPES = {
    'F': (SOUTH, EAST),
    'J': (NORTH, WEST),
    '|': (SOUTH, NORTH),
    '-': (WEST, EAST),
    '7': (SOUTH, WEST),
    'L': (NORTH, EAST),
    '.': (),
    'S': (NORTH, WEST, SOUTH, EAST)
}
DIRECTIONS = {
    NORTH: (0, -1),
    WEST: (-1, 0),
    EAST: (1, 0),
    SOUTH: (0, 1)
}
WIDTH,HEIGHT = len(lines[0]), len(lines)
SEP = -1
i = 0
batch = [start, SEP]
visited = [ [False]*len(lines[0]) for i in range(len(lines))]
visited[start[1]][start[0]] = True
while len(batch) > 0:
    pos = batch.pop(0)
    if pos == SEP:
        i += 1
        if len(batch) > 0:
            batch.append(SEP)
        continue
    
    x,y = pos
    pipe = lines[y][x]
    for dir in PIPES[pipe]:
        mvx, mvy = DIRECTIONS[dir]
        nx,ny = x+mvx, y+mvy
        if WIDTH > nx >= 0 and HEIGHT > ny >= 0 and not visited[ny][nx]:
            visited[ny][nx] = True
            batch.append((nx, ny))

print(i)
        