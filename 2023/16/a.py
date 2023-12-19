NORTH = 0
WEST = 1
SOUTH = 2
EAST = 3

OBSTACLES = {
    '\\': {
        EAST: [SOUTH],
        NORTH: [WEST],
        SOUTH: [EAST],
        WEST: [NORTH]
    },
    '/': {
        NORTH: [EAST],
        SOUTH: [WEST],
        EAST: [NORTH],
        WEST: [SOUTH],
    },
    '|': {
        NORTH: [NORTH],
        SOUTH: [SOUTH],
        WEST: [NORTH, SOUTH],
        EAST: [NORTH, SOUTH]
    },
    '-': {
        WEST: [WEST],
        EAST: [EAST],
        NORTH: [WEST, EAST],
        SOUTH: [WEST, EAST]
    },
    '.': {
        SOUTH: [SOUTH],
        WEST: [WEST],
        NORTH: [NORTH],
        EAST: [EAST]
    }
}

DIRECTIONS = {
    WEST: [-1, 0],
    SOUTH: [0,1],
    EAST: [1,0],
    NORTH: [0,-1]
}


batch = [(0,0,EAST)]
lines = list(map(lambda x: x.strip(), open('input', 'r').readlines()))
W,H = len(lines[0]), len(lines)
visited = [[[False]*4 for j in range(W)] for i in range(H)]
visited[0][0][EAST] = True

while len(batch) > 0:
    x,y,heading = batch.pop(0)
    stading_on = lines[y][x]
    for new_direction in OBSTACLES[stading_on][heading]:
        dx,dy = DIRECTIONS[new_direction]
        nx,ny = x+dx, y+dy
        if not (W > nx >= 0 and H > ny >= 0) or visited[ny][nx][new_direction]:
            continue
        visited[ny][nx][new_direction] = True
        batch.append((nx, ny, new_direction))

total = 0
for x in range(W):
    for y in range(H):
        if any(visited[y][x]):
            total += 1

print(total)
