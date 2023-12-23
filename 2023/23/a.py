from sys import setrecursionlimit
setrecursionlimit(10**8)

NORTH = 0
SOUTH = 2
WEST = 3
EAST = 1
ARROWS = ['^', '>', 'v', '<']

def main(x, y, visited):
    if (x,y) == end:
        return 1
    
    visited[y][x] = True
    best = float('-inf')
    for nx, ny, dr in [(x+1, y, EAST), (x-1,y, WEST), (x,y+1, SOUTH), (x,y-1, NORTH)]:
        if not (W > nx >= 0 and H > ny >= 0) or visited[ny][nx] or lines[ny][nx] == '#':
            continue
        if lines[ny][nx] in ARROWS and ARROWS[dr] != lines[ny][nx]:
            continue

        best = max(main(nx, ny, visited), best)
    
    visited[y][x] = False
    return best + 1
        

lines = list(map(lambda x: x.strip(), open('input', 'r').readlines()))
W,H = len(lines[0]), len(lines)
start = (1,0)
end = (W-2, H-1)
print(main(1, 0, [[False]*W for i in range(H)])-1)