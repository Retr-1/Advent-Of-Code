from inputifyle import *
read('input')

blocks = {
    'red':12,
    'green':13,
    'blue':14
}

def check(line):
    for subgame in line.split(';'):
        for block in subgame.split(','):
            count,color = block.split()
            if blocks[color] < int(count):
                return False
    return True

good = 0
i = 1
while (line:=input()) != '':
    if check(line.split(':')[1]):
        good += i

    i += 1

print(good)


