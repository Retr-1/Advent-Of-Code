lines = list(map(lambda x: x.strip(), open('input', 'r').readlines()))
groups = []
world = []
for line in lines:
    a,b = line.split('~')
    start = list(map(int, a.split(',')))
    end = list(map(int, b.split(',')))
    this = []
    for x in range(min(start[0], end[0]), max(start[0], end[0])+1):
        for y in range(min(start[1], end[1]), max(start[1], end[1])+1):
            for z in range(min(start[2], end[2]), max(start[2], end[2])+1):
                block = [x,y,z]
                this.append(block)
                world.append(block)
    groups.append(this)

while True:
    static = True

    for group in groups:
        for block in group:
            if block[2] == 0:
                break
            new_block = [block[0], block[1], block[2]-1]
            if not new_block in group and new_block in world:
                break
        else:
            for block in group:
                block[2] -= 1
            static = False
    
    if static:
        break

total = 0
for group in groups:
    for block in group:
        new_block = [block[0], block[1], block[2]+1]
        if not new_block in group and new_block in world:
            break
    else:
        total += 1

print(total)
