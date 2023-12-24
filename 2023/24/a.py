from itertools import combinations

def find_intersection(line1, line2):
    x1, y1, dx1, dy1 = line1
    x2, y2, dx2, dy2 = line2

    det = dx1 * -dy2 - -dx2 * dy1

    if det == 0:
        return None
    

    px = ((x2 - x1) * -dy2 - -dx2*(y2-y1)) / det
    py = (dx1*(y2-y1) - (x2-x1)*dy1) / det

    return px,py



textlines = map(lambda x: x.strip(), open('input', 'r').readlines())
lines = []
LEFT = 200000000000000
RIGHT = 400000000000000
for textline in textlines:
    a,b = textline.split('@')
    x,y,z = map(int, a.split(','))
    vx,vy,vz = map(int, b.split(','))
    lines.append(((x,y,z,vx,vy,vz)))

total = 0
for la, lb in combinations(lines, 2):
    x1,y1,z1,vx1,vy1,vz1 = la
    x2,y2,z2,vx2,vy2,vz2 = lb

    res = find_intersection((x1,y1,vx1,vy1), (x2,y2,vx2,vy2))
    if not res:
        continue
    px,py = res
    if RIGHT >= px >= LEFT and RIGHT >= py >= LEFT:
        total += 1


        

print(total)