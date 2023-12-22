lines = list(map(lambda x: x.strip(), open('input', 'r').readlines()))
W,H = len(lines[0]), len(lines)
for y,line in enumerate(lines):
    if line.find('S') != -1:
        start = (line.find('S'),y)

batch = [start]
new_batch = set()
for i in range(64):
    while len(batch) > 0:
        x,y = batch.pop(0)
        for nx,ny in [[x+1,y], [x-1,y], [x,y+1], [x,y-1]]:
            if not (W > nx >= 0 and H > ny >= 0) or lines[ny][nx] == '#':
                continue
            new_batch.add((nx,ny))
    batch = list(new_batch)
    new_batch = set()

print(len(batch), (69,63) in batch)



    