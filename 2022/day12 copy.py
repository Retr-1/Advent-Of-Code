from mycode import getlines

grid = getlines('input12')
BASIC_MOVES = ((1,0),(0,1),(-1,0),(0,-1))

for i in range(len(grid)):
    if grid[i].find('S') != -1:
        START = (grid[i].find('S'),i)
        grid[i] = grid[i][:START[0]] + 'a' + grid[i][START[0]+1:]

    if grid[i].find('E') != -1:
        END = (grid[i].find('E'),i)
        grid[i] = grid[i][:END[0]] + 'z' + grid[i][END[0]+1:]

visited = set()
batch = [(END,0)]

while True:
    pos,moves = batch.pop(0)

    if grid[pos[1]][pos[0]] == 'a':
        print(moves)
        exit()

    for dx,dy in BASIC_MOVES:
        #print(grid[pos[1]+dy][pos[0]+dx],grid[pos[1]][pos[0]])
        if len(grid[0]) > pos[0]+dx >= 0 and len(grid) > pos[1]+dy >= 0 and ord(grid[pos[1]+dy][pos[0]+dx])-ord(grid[pos[1]][pos[0]]) >= -1 and (not (pos[0]+dx,pos[1]+dy) in visited):
            visited.add((pos[0]+dx,pos[1]+dy))
            batch.append(((pos[0]+dx,pos[1]+dy),moves+1))