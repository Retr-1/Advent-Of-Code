from mycode import readfromfile

def getpriority(letter):
    o = ord(letter)
    if o < 91:
        return o-65+27
    return o-97+1

s = 0
for val in readfromfile('input3'):
    contains = [False]*58
    for i in range(len(val)//2):
        contains[ord(val[i])-65] = True
    
    for i in range(len(val)//2,len(val)):
        if contains[ord(val[i])-65]:
            #print(val[i], getpriority(val[i]))
            s += getpriority(val[i])
            break

print(s)