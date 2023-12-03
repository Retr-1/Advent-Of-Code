from mycode import readfromfile
from collections import deque

def intializer(string,splitter=' '):
    return tuple(map(lambda x: int(x) ,string.split(splitter)))

occupied = set()
cubes = []

for line in readfromfile('input18'):
    line = intializer(line,',')
    occupied.add(line)
    cubes.append(line)


BORDERS = [
    [float('inf'),float('-inf')],
    [float('inf'),float('-inf')],
    [float('inf'),float('-inf')]
]
for cube in cubes:
    for i in range(3):
        BORDERS[i][0] = min(cube[i], BORDERS[i][0])
        BORDERS[i][1] = max(cube[i], BORDERS[i][1])

for i in range(3):
    BORDERS[i][0] -= 1
    BORDERS[i][1] += 1

START = (BORDERS[0][0],BORDERS[1][0],BORDERS[2][0])
batch = deque([START])
visited = set()

area = 0
while len(batch) > 0:
    x,y,z = batch.popleft()
    for dx,dy,dz in ((-1,0,0),(1,0,0),(0,0,-1),(0,0,1),(0,1,0),(0,-1,0)):
        newpos = (x+dx,y+dy,z+dz)
        if newpos in occupied:
            area += 1
        elif BORDERS[0][1] >= newpos[0] >= BORDERS[0][0] and BORDERS[1][1] >= newpos[1] >= BORDERS[1][0] and BORDERS[2][1] >= newpos[2] >= BORDERS[2][0] and (not (newpos in visited)):
            batch.append(newpos)
            visited.add(newpos)

print(area)