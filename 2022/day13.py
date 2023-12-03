from mycode import readfromfile
import json

intel = readfromfile('input13')

def compare(a,b):
    for i in range(len(a)):
        if i == len(b):
            return -1

        if type(a[i]) == int and type(b[i]) == int:
            if a[i] != b[i]:
                return 1 if a[i] < b[i] else -1
            continue

        v = compare([a[i]] if type(a[i])!=list else a[i], [b[i]] if type(b[i])!=list else b[i])
        if v != 0:
            return v

    return 0 if len(a)==len(b) else 1

#compare([1,1,3,1,1],[1,1,5,1,1])
c = 0
i = 0
try:
    while True:
        i += 1
        a = json.loads(next(intel))
        b = json.loads(next(intel))
        next(intel)

        if compare(a,b)==1:
            c += i
except:
    print(c)