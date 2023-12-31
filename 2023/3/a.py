from inputifyle import *
read('input')

def check_validity(x, y, lines):
    for nx, ny in ((x+1, y+1), (x+1, y), (x+1, y-1), (x, y+1), (x, y-1), (x-1, y+1), (x-1, y), (x-1, y-1)):
        if (not (len(lines) > ny >= 0 and len(lines[ny]) > nx >= 0)) or lines[ny][nx].isdigit():
            continue

        if lines[ny][nx] != '.':
            return True
    
    return False

lines = []
while (x:=input()) != '':
    lines.append(x.strip())

total = 0

for y in range(len(lines)):
    number = ''
    is_valid = False

    for x in range(len(lines[y])):
        letter = lines[y][x]

        if letter.isdigit():
            number += letter
            is_valid = is_valid or check_validity(x, y, lines)
        else:
            if number != '' and is_valid:
                # print(number)
                total += int(number)
                       
            number = ''
            is_valid = False

    if number != '' and is_valid:
        total += int(number)

print(total)
