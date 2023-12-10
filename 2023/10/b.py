from math import floor, ceil

def are_connected_horizontal(pipe_left, pipe_right):
    return EAST in PIPES[pipe_left] and WEST in PIPES[pipe_right]

def are_connected_vertical(pipe_up, pipe_down):
    return SOUTH in PIPES[pipe_up] and NORTH in PIPES[pipe_down]

def BFS(x, y, overvisited, visited):
    if (x,y) in overvisited:
        return
    
    batch = [(x,y)]
    while len(batch) > 0:
        x,y = batch.pop(0)
        for nx, ny, dir in ((x+.5, y, EAST), (x-.5, y, WEST), (x, y+.5, SOUTH), (x, y-.5, NORTH)):
            if not (WIDTH > nx >= 0 and HEIGHT > ny >= 0) or (nx, ny) in overvisited:
                continue

            if not (nx.is_integer() or ny.is_integer()):
                overvisited.add((nx,ny))
                batch.append((nx,ny))
                continue

            if not nx.is_integer():
                nx_low = floor(nx)
                nx_high = ceil(nx)
                ny = int(ny)

                if visited[ny][nx_low] and visited[ny][nx_high] and are_connected_horizontal(lines[ny][nx_low], lines[ny][nx_high]):
                    continue
            
            if not ny.is_integer():
                ny_low = floor(ny)
                ny_high = ceil(ny)
                nx = int(nx)

                if visited[ny_low][nx] and visited[ny_high][nx] and are_connected_vertical(lines[ny_low][nx], lines[ny_high][nx]):
                    continue

            if nx.is_integer() and ny.is_integer() and visited[int(ny)][int(nx)]:
                continue
            
            overvisited.add((nx,ny))
            batch.append((nx,ny))

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

# overvisited = [ [visited[i][j] for j in range(WIDTH)] for i in range(HEIGHT)]
overvisited = set() #[ [False]*WIDTH for i in range(HEIGHT)]
for x in range(WIDTH):
    BFS(x, 0, overvisited, visited)
    BFS(x, HEIGHT-1, overvisited, visited)
for y in range(HEIGHT):
    BFS(0, y, overvisited, visited)
    BFS(WIDTH-1, y, overvisited, visited)

i = 0
for y in range(HEIGHT):
    for x in range(WIDTH):
        if not (x,y) in overvisited and not visited[y][x]:
            i += 1

print(i)

        
        