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

snake = [[0,0]] + [(0,0)]*9
actions = {

}

for n,line in enumerate(inlet):
    mv,c = line.split()
    c = int(c)
    cmv = moves[mv]


    for i in range(c):
        
        snake[0][0] += cmv[0]
        snake[0][1] += cmv[1]

        for j in range(1,10):
            dx = snake[j-1][0]-snake[j][0]
            dy = snake[j-1][1]-snake[j][1]

            if abs(dx)<=1 and abs(dy)<=1:
                continue

            if abs(dx)==2 and abs(dy)==2:
                snake[j] = (snake[j][0]+dx//2, snake[j][1]+dy//2)
            elif abs(dx) <= 1:
                snake[j] = (snake[j][0]+dx, snake[j][1]+dy//2)
            else:
                snake[j] = (snake[j][0]+dx//2, snake[j][1]+dy)

        
            #print(head,tail)
        #print(mv,snake)
        visited.add(snake[-1])


print(len(visited))
