from mycode import readfromfile,intializer


s = 0
for line in readfromfile('input4'):
    elf1,elf2 = line.split(',')
    a,b = intializer(elf1,'-')
    x,y = intializer(elf2,'-')

    if (a<=x and b>=y) or (x<=a and y>=b):
        s += 1

print(s)