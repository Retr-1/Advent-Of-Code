lines = list(map(lambda x: x.strip(), open('input', 'r').readlines()))

total = 0
scratches = [None]*len(lines)
scratches[len(lines)-1] = 1

for g in range(len(lines)-1, -1, -1):
    game = lines[g]
    my, win = game.split(':')[1].split('|')
    my = set(my.split())
    win = set(win.split())
    diff = len(my.intersection(win))
    t = 0
    for j in range(diff):
        t += scratches[g+j+1]+1
    scratches[g] = t

# print(scratches)
print(sum(scratches) + len(lines))