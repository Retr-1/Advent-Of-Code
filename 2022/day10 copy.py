from mycode import readfromfile

intel = readfromfile('input10')

def paint(visible):
    pass

def pos(cycle):
    return cycle%40, cycle//40

def paint():
    x,y = pos(cycle-1)
    if y>= 6: return
    display[y] += '#' if x == register or x == register-1 or x == register+1 else '.'

def make_instructions(filename,display):
    f = open(filename,'w')
    cycle = 0
    acycle = 0
    register = 1

    while cycle < 240:
        # Get the good ones
        while True:
            x,y = pos(acycle)
            distance = abs(register-acycle)
            if y >=6 or (display[y][x] == '#' and distance >= 2) or (display[y][x] == '.' and distance < 2):
                break
            acycle += 1

        if acycle-cycle <= 1:
            raise Exception('Cannot Happen')

        # write noop
        for i in range(acycle-cycle-2):
            f.write('noop\n')

        #Find move pos - first #
        while True:
            x,y = pos(acycle)
            if y>= 6 or display[y][x] == '#':
                acycle += 1
                break
            acycle += 1

        f.write(f'addx {(x+1)-register}\n')
        register = x+1
        cycle = acycle

    f.close()

def make_instructions2(filename,display):
    pass


cycle = 0
register = 1
display = ['']*6

for line in intel:
    line = line.split()
    
    if line[0] == 'addx':        
        cycle += 1
        paint()
        cycle += 1
        paint()
    else:
        cycle += 1
        paint()

    
    if line[0] == 'addx':
        register += int(line[1])

# for x in display:
#     print(x)

make_instructions('instructions',display)
    