from mycode import getlines,readfromfile
from collections import defaultdict

inlet = getlines('input5.txt')

drawend = inlet.index('')
n = (len(inlet[drawend-1])+1)//4
crates = [[] for x in range(n)]

# crates = defaultdict(lambda: [])



for i in range(drawend-1):
    line = inlet[i]    
    for c,i in enumerate(range(1,len(line),4)):
        if line[i] != ' ':
            crates[c].append(line[i])

for line in inlet[drawend+1:]:
    if line == '': break
    line = line.split()
    count = int(line[1])
    frm = int(line[3])-1
    to = int(line[5])-1

    removed = crates[frm][:count]
    removed.reverse()
    crates[frm][:count] = []
    crates[to][:0] = removed

s = ''
for i in range(n):
    s += crates[i][0]

print(s)
