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
visited = [ [ [[False]*7,[False]*7,[False]*7,[False]*7] for j in range(W)] for i in range(H)]
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
        if new_direction == (heading+2)%4 or heading == new_direction:
            continue

        dx, dy = DIRECTIONS[new_direction]
        nx, ny = x, y
        valid = True
        new_cost = cost

        for i in range(4):
            nx += dx
            ny += dy
            if not (W > nx >= 0 and H > ny >= 0):
                valid = False
                break
            new_cost += lines[ny][nx]

        if not valid:
            continue

        for new_consecutive in range(7):
            if new_consecutive > 0:
                nx += dx
                ny += dy

                if not (W > nx >= 0 and H > ny >= 0):
                    break

                new_cost += lines[ny][nx]


            if not visited[ny][nx][new_direction][new_consecutive]:
                heappush(heap, (new_cost, nx, ny, new_consecutive, new_direction))
    # print(len(heap))

