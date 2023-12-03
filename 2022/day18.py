from mycode import readfromfile

def intializer(string,splitter=' '):
    return tuple(map(lambda x: int(x) ,string.split(splitter)))

occupied = set()
cubes = []

for line in readfromfile('input18'):
    line = intializer(line,',')
    occupied.add(line)
    cubes.append(line)

area = 0
cubes = [[2,2,5]]
for x,y,z in cubes:
    for dx,dy,dz in ((-1,0,0),(1,0,0),(0,0,-1),(0,0,1),(0,1,0),(0,-1,0)):
        if not (x+dx,y+dy,z+dz) in occupied:
            area += 1

print(area)