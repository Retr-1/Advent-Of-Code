lines = list(map(lambda x: x.strip(), open('input', 'r').readlines()))

total = 0

for game in lines:
    my, win = game.split(':')[1].split('|')
    
    n = len(set(my.split()).intersection(set(win.split())))
    if n > 0:
        total += 2**(n-1)

print(total)