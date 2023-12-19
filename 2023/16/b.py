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

def get_score(x,y,heading):
    batch = [(x,y,heading)]
    visited = [[[False]*4 for j in range(W)] for i in range(H)]
    visited[x][y][heading] = True

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

    return total


lines = list(map(lambda x: x.strip(), open('input', 'r').readlines()))
W,H = len(lines[0]), len(lines)

best = 0
for x in range(W):
    best = max(best, get_score(x, 0, SOUTH), get_score(x, H-1, NORTH))
for y in range(H):
    best = max(best, get_score(0, y, EAST), get_score(W-1, y, WEST))
print(best)
