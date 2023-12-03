from inputifyle import *
read('input')

blocks = {
    'red':12,
    'green':13,
    'blue':14
}

def check(line):
    sufficient = {
        'red':0,
        'green':0,
        'blue':0
    }
    for subgame in line.split(';'):
        for block in subgame.split(','):
            count,color = block.split()
            sufficient[color] = max(sufficient[color], int(count))
        
    return sufficient['red']*sufficient['green']*sufficient['blue']

good = 0
i = 1
while (line:=input()) != '':
    good += check(line.split(':')[1])

print(good)


