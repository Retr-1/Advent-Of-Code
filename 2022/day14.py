from mycode import readfromfile

intel = readfromfile('input14')
blocks = set()

def ext(pos):
    a,b = pos.strip().split(',')
    return (int(a),int(b))

def sign(x):
    if x > 0: return 1
    if x < 0: return -1
    return 0

for line in intel:
    poses = line.split('->')
    for i in range(1,len(poses)):
        curr = ext(poses[i])
        prev = ext(poses[i-1])

        dx = abs(curr[0]-prev[0])
        dy = abs(curr[1]-prev[1])
        mv = max(dx,dy)

        mvx = (curr[0]-prev[0]) // mv
        mvy = (curr[1]-prev[1]) // mv

        for j in range(max(dx,dy)+1):
            blocks.add((prev[0]+mvx*j, prev[1]+mvy*j))

VOID = max(blocks,key=lambda x: x[1])[1]

def fall_sand():
    px = 500
    py = 0

    while py <= VOID:
        if not (px,py+1) in blocks:
            py += 1
        elif not (px-1,py+1) in blocks:
            px -= 1
            py += 1
        elif not (px+1,py+1) in blocks:
            px += 1
            py += 1
        else:
            blocks.add((px,py))
            return True
    
    return False

i = 0
while fall_sand():
    i += 1

print(i)
