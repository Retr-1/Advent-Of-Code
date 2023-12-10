def BFS(start, visited):
    if visited[start[1]][start[0]]:
        return
    
    batch = [start]
    while len(batch) > 0:
        x,y = batch.pop(0)
        for nx, ny in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            if not (WIDTH > nx >= 0 and HEIGHT > ny >= 0) or visited[ny][nx]:
                continue

            visited[ny][nx] = True
            batch.append((nx,ny))

lines = list(map(lambda x: x.strip(), open('test5', 'r').readlines()))

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
i = -1
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
    curr_pipe = lines[y][x]
    for nx, ny, dir in ((x+1, y, EAST), (x-1, y, WEST), (x, y+1, SOUTH), (x, y-1, NORTH)):
        if not (WIDTH > nx >= 0 and HEIGHT > ny >= 0):
            continue
        next_pipe = lines[ny][nx]
        if dir in PIPES[curr_pipe] and (dir+2)%4 in PIPES[next_pipe] and not visited[ny][nx]:
            visited[ny][nx] = True
            batch.append((nx,ny))

overvisited = [ [visited[i][j] for j in range(WIDTH)] for i in range(HEIGHT)]
for x in range(WIDTH):
    BFS((x, 0), overvisited)
    BFS((x, HEIGHT-1), overvisited)
for y in range(HEIGHT):
    BFS((0, y), overvisited)
    BFS((WIDTH-1, y), overvisited)

i = 0
for y in range(HEIGHT):
    for x in range(WIDTH):
        if not overvisited[y][x]:
            i += 1

print(i)

        
        