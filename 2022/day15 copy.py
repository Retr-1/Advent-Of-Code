from mycode import readfromfile

intel = readfromfile('input15')
sensors = []
monuments = [0]

def whiledigit(string:str,i):
    while i < len(string) and (string[i].isdigit() or string[i]=='-'):
        i += 1
    return i

def extractdigit(string,i):
    j = whiledigit(string,i)
    return int(string[i:j])

for line in intel:
    if line == '': break
    x = extractdigit(line,line.find('x')+2)
    y = extractdigit(line,line.find('y')+2)
    
    m = extractdigit(line,line.rfind('x')+2)
    n = extractdigit(line,line.rfind('y')+2)
    d = abs(x-m)+abs(y-n)
    sensors.append((x,y,d))

    for x in [1,-1,0]:
        p = y+x*d+x
        if p >= 0:
            monuments.append(p)


def binary_search(start,end):
    while True:
        if start == end:
            return start

        pos = start + (end-start)//2
        if check(pos) is None:
            start = pos+1
        else:
            end = pos

def check(i):
    intervals = []

    for x,y,d in sensors:
        avaible = d-abs(y-i)
        if avaible >= 0:
            intervals.append((x-avaible,x+avaible))

    intervals.sort(key=lambda x: x[0])
    current = intervals[0]
    for x in intervals[1:]:
        if current[1]+1 >= x[0]:
            current = current[0],max(x[1],current[1])
        else:
            return current[1]+1
    
    # if current[0]-1 > 0:
    #     return 0
    
    # if current[1]+1 < 40000:
    #     return current[1]+1
    
    return None

monuments = list(set(monuments))
monuments.sort()
monuments.pop()

for i in range(len(monuments)):
    r = check(monuments[i])
    if r is None:
        continue
    if i == 0:
        print(r)
        break

    r = binary_search(monuments[i-1],monuments[i])
    print(check(r),r)
    break