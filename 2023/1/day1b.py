from inputifyle import *
read('input1a')

total = 0
numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'] 

while (t:=input()) != '':
    num = ''

    low = (float('inf'), None)
    high = (float('-inf'), None)

    for i in range(len(t)):
        if t[i].isdigit():
            low = (i, int(t[i]))
            break

    for n, x in enumerate(numbers):
        if (i:=t.find(x)) != -1:
            low = min(low, (i, n+1))
    
    for i in range(len(t)-1,-1,-1):
        if t[i].isdigit():
            high = (i, int(t[i]))
            break

    for n, x in enumerate(numbers):
        if (i:=t.rfind(x)) != -1:
            high = max(high, (i, n+1))
    
    total += low[1]*10 + high[1]

print(total)