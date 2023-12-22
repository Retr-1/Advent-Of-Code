def BFS(x, y, i=0):
    visited = [[False]*W for i in range(H)]
    visited[y][x] = True
    batch = [(x,y), (None,None)]
    c = 0
    while len(batch) > 0:
        x,y = batch.pop(0)

        if x==None:
            if len(batch) > 0:
                batch.append((None,None))
            i += 1
            if i == 64:
                break
            continue


        if i%2 == 1:
            c += 1


        for nx,ny in [[x+1,y], [x-1,y], [x,y+1], [x,y-1]]:
            if not (W > nx >= 0 and H > ny >= 0) or lines[ny][nx] == '#' or visited[ny][nx]:
                continue
            batch.append((nx,ny))
            visited[ny][nx] = True

    return visited, i, c




lines = list(map(lambda x: x.strip(), open('input', 'r').readlines()))
W,H = len(lines[0]), len(lines)



for y,line in enumerate(lines):
    if line.find('S') != -1:
        start = (line.find('S'),y)

print(BFS(W-1, start[1]))
# print(len(batch))



    