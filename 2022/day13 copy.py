from mycode import readfromfile
import json
import functools

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
packets = []
try:
    while True:
        a = json.loads(next(intel))
        b = json.loads(next(intel))
        packets.append(a)
        packets.append(b)
        next(intel)
except:
    pass

def fff(x,y):
    print(x,y) # ak vysledok zaporny, tak to nalavo, ak je vysledok kladny to napravo
    return y-x

#packets.sort(key=functools.cmp_to_key(lambda x,y: -1 if compare(x,y)==1 else 1))

v1 = 1
for x in packets:
    if compare(x,[[2]])==1:
        v1 += 1

v2 = 2
for x in packets:
    if compare(x,[[6]])==1:
        v2 += 1

print(v1*v2)