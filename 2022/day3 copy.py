from mycode import getlines

def getpriority(letter):
    o = ord(letter)
    if o < 91:
        return o-65+27
    return o-97+1

s = 0
inlet = getlines('input3')
print(len(inlet))

for i in range(0,len(inlet),3):
    contains = [0]*52
    for x in inlet[i]:
        contains[getpriority(x)-1] = 1
    for x in inlet[i+1]:
        if contains[getpriority(x)-1] == 1:
            contains[getpriority(x)-1] = 2
    for x in inlet[i+2]:
        if contains[getpriority(x)-1] == 2:
            #print(x)
            s += getpriority(x)
            break

print(s)