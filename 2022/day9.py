from mycode import readfromfile

inlet = readfromfile('input9')

head = [0,0]
tail = [0,0]

visited = set()

moves = {
    'R':[1,0],
    'L':[-1,0],
    'U':[0,-1],
    'D':[0,1]
}

for line in inlet:
    mv,c = line.split()
    c = int(c)

    cmv = moves[mv]
    # head[0] += cmv[0]*c
    # head[1] += cmv[1]*c

    for i in range(c):
        head[0] += cmv[0]
        head[1] += cmv[1]

        dx = abs(tail[0]-head[0])
        dy = abs(tail[1]-head[1])

        if dx<=1 and dy<=1:
            continue

        tail = [head[0]+cmv[0]*-1, head[1]+cmv[1]*-1]
        #print(head,tail)
        visited.add(tuple(tail))


print(len(visited)+1)
