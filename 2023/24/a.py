from itertools import combinations

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
    # x1 + vx1*t = x2 + vx2*t
    # y1 + vy1*t = y2 + vy2*t
    # (x2 - x1) / (vx1 - vx2) = t
    x1,y1,z1,vx1,vy1,vz1 = la
    x2,y2,z2,vx2,vy2,vz2 = lb

    # if vx1 == vx2:
    #     if x1 != x2:
    #         continue
    #     if vy1 == vy2:
    
    
    
    tx = (x2 - x1) / (vx1 - vx2)
    ty = (y2 - y1) / (vy1 - vy2)


        

print(total)