from inputifyle import *
read('input')
from collections import defaultdict

def check_validity(x, y, lines):
    valid = False
    gs = set()

    for nx, ny in ((x+1, y+1), (x+1, y), (x+1, y-1), (x, y+1), (x, y-1), (x-1, y+1), (x-1, y), (x-1, y-1)):
        if (not (len(lines) > ny >= 0 and len(lines[ny]) > nx >= 0)) or lines[ny][nx].isdigit():
            continue

        if lines[ny][nx] != '.':
            valid = True

        if lines[ny][nx] == '*':
            gs.add((nx,ny))
    
    return valid,gs

lines = []
while (x:=input()) != '':
    lines.append(x.strip())

total = 0
gears = defaultdict(list)

for y in range(len(lines)):
    number = ''
    is_valid = False
    current_gears = set()

    for x in range(len(lines[y])):
        letter = lines[y][x]

        if letter.isdigit():
            number += letter
            a,b = check_validity(x, y, lines)
            is_valid = is_valid or a
            current_gears.update(b)
        else:
            if number != '' and is_valid:
                n = int(number)
                # print(number)
                total += int(number)
                for pos in current_gears:
                    gears[pos].append(n)
                       
            number = ''
            current_gears = set()
            is_valid = False

    if number != '' and is_valid:
        total += int(number)
        n = int(number)
        for pos in current_gears:
            gears[pos].append(n)

print('part1', total)

total = 0
for g in gears:
    if len(gears[g]) == 2:
        a,b = gears[g]
        total += a*b

print('part2', total)

