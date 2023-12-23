from sys import setrecursionlimit
setrecursionlimit(10**8)


def main(x, y, visited, dead_end):
    if (x,y) == end:
        return 1
    
    if dead_end[y][x]:
        return float('-inf')
    
    visited[y][x] = True
    best = float('-inf')
    for nx, ny in [(x+1, y), (x-1,y), (x,y+1), (x,y-1)]:
        if not (W > nx >= 0 and H > ny >= 0) or visited[ny][nx] or lines[ny][nx] == '#':
            continue

        best = max(main(nx, ny, visited, dead_end), best)
    
    visited[y][x] = False
    if best == float('-inf'):
        dead_end[y][x] = True
        
    return best + 1
        

lines = list(map(lambda x: x.strip(), open('test', 'r').readlines()))
W,H = len(lines[0]), len(lines)
start = (1,0)
end = (W-2, H-1)
print(main(1, 0, [[False]*W for i in range(H)], [[False]*W for i in range(H)])-1)