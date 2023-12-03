from inputifyle import *
read('input1a')

total = 0
while (t:=input()) != '':
    num = ''

    for i in range(len(t)):
        if t[i].isdigit():
            num += t[i]
            break

    for i in range(len(t)-1,-1,-1):
        if t[i].isdigit():
            num += t[i]
            break
    
    total += int(num)

print(total)