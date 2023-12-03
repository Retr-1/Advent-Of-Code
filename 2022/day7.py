from mycode import readfromfile
#from typing import NamedTuple

directory = {}
intel = readfromfile('input7')
stack = []

s = 0
lsd = False

for line in intel:
    line = line.split()

    if lsd:
        if '$' == line[0]:
            lsd = False
        else:
            if line[0] != 'dir':
                stack[-1] += int(line[0])
            continue

    if 'cd' in line:
        if '..' in line:
            val = stack.pop()
            if val < 100000:
                s += val
            if stack: stack[-1] += val
        else:
            stack.append(0)
    elif 'ls' in line:
        lsd = True

for i in range(len(stack)):
    val = stack.pop()
    if val < 100000:
        s += val
    if stack: stack[-1] += val
            
print(s,stack)