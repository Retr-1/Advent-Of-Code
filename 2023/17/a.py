from heapq import heappush, heappop

NORTH = 0
WEST = 1
SOUTH = 2
EAST = 3

DIRECTIONS = {
    WEST: [-1, 0],
    SOUTH: [0,1],
    EAST: [1,0],
    NORTH: [0,-1]
}

lines = list(map(lambda x: list(map(int, list(x.strip()))), open('input', 'r').readlines()))
W,H = len(lines[0]), len(lines)
heap = [(0, 0, 0, 0, -1)]
visited = [ [ [[False]*3,[False]*3,[False]*3,[False]*3] for j in range(W)] for i in range(H)]
# visited[0][0] = float('inf')

while True:
    cost, x, y, consecutive, heading = heappop(heap)

    if visited[y][x][heading][consecutive]:
        continue

    visited[y][x][heading][consecutive] = True

    if x == W-1 and y == H-1:
        print(cost)
        break

    for new_direction in DIRECTIONS:
        dx, dy = DIRECTIONS[new_direction]
        nx, ny = x+dx, y+dy
        if not (W > nx >= 0 and H > ny >= 0) or new_direction == (heading+2)%4:
            continue
        new_consecutive = 0 if new_direction != heading else consecutive+1
        if new_consecutive >= 3:
            continue
        
        if not visited[ny][nx][new_direction][new_consecutive]:
            heappush(heap, (cost+lines[ny][nx], nx, ny, new_consecutive, new_direction))

