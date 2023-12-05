def extract_conversions(lines):
    a = []
    b = []
    for line in lines:
        if line.find(':') != -1:
            continue

        if line == '':
            if b:
                b.sort(key=lambda x: x[0][0])
                a.append(tuple(b))
                b.clear()
        else:
            e,f,g = map(int, line.split())
            dest = (e, e+g)
            source = (f, f+g)
            b.append((source, dest))
    if b:
        b.sort()
        a.append(tuple(b))
        b.clear()

    return a

def find_dest(i, conversions, loc):    
    for j in range(len(conversions[i])):
        if conversions[i][j][0][1] > loc >= conversions[i][j][0][0]:
            diff = loc - conversions[i][j][0][0]
            assert diff >= 0
            return conversions[i][j][1][0]+diff
        
    return loc

lines = list(map(lambda x: x.strip(), open('input', 'r').readlines()))
seeds = list(map(int, lines[0].split(':')[1].split()))
# print(list(seeds))
conversions = extract_conversions(lines[1:])

# t = 9 + 7
# for x in conversions:
#     t += len(x)
# print(t)

best = float('inf')
for x in range(0, len(seeds), 2):
    print(x)
    for loc in range(seeds[x], seeds[x]+seeds[x+1]):
        for i in range(len(conversions)):
            loc = find_dest(i, conversions, loc)
        best = min(best, loc)

print(best)
    
