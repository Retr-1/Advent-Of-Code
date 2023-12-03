from mycode import readfromfile

intel = readfromfile('input15')
sensors = []

def whiledigit(string:str,i):
    while i < len(string) and (string[i].isdigit() or string[i]=='-'):
        i += 1
    return i

total = 0
ROW = 2000000
beacons = set()

def extractdigit(string,i):
    j = whiledigit(string,i)
    return int(string[i:j])

for line in intel:
    if line == '': break
    x = extractdigit(line,line.find('x')+2)
    y = extractdigit(line,line.find('y')+2)
    
    m = extractdigit(line,line.rfind('x')+2)
    n = extractdigit(line,line.rfind('y')+2)
    sensors.append((x,y,abs(x-m)+abs(y-n)))
    beacons.add((m,n))

intervals = []

for x,y,d in sensors:
    avaible = d-abs(y-ROW)
    if avaible >= 0:
        intervals.append((x-avaible,x+avaible))

intervals.sort(key=lambda x: x[0])
current= intervals[0]
for x in intervals[1:]:
    if current[1] >= x[0]:
        current = current[0],max(x[1],current[1])
    else:
        total += current[1]-current[0]+1
        current = x
total += current[1]-current[0]+1
for beacon in beacons:
    if beacon[1] == ROW:
        total -= 1
print(total)
