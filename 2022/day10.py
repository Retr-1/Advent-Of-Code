from mycode import readfromfile

intel = readfromfile('input10')

cycle = 0
next_cycle = 20
register = 1
toadd = 0
mx = float('-inf')
mn = float('inf')
s = 0
for line in intel:
    line = line.split()
    
    if line[0] == 'addx':        
        cycle += 2
    else:
        cycle += 1

    if cycle>=next_cycle:
        s += next_cycle*register
        #print(register)
        next_cycle += 40

        if next_cycle > 220:
            break
    
    if line[0] == 'addx':
        register += int(line[1])
        mx = max(mx,register)
        mn = min(mn,register)

print(mx,mn)
print(s)
    