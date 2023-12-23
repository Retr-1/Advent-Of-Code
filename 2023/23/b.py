from sys import setrecursionlimit
setrecursionlimit(10**8)

def simplify(x, y):
    for nx, ny, dr in [(x+1, y), (x-1,y), (x,y+1), (x,y-1)]:
        if not (W > nx >= 0 and H > ny >= 0) or lines[ny][nx] == '#':
            continue



lines = list(map(lambda x: x.strip(), open('test', 'r').readlines()))
W,H = len(lines[0]), len(lines)
start = (1,0)
end = (W-2, H-1)
