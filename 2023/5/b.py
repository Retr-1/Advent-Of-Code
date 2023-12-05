def extract_conversions(lines):
    a = []
    b = []
    for line in lines:
        if line.find(':') != -1:
            continue

        if line == '':
            if b:
                b.sort(key=lambda x: x[0][0])
                a.append(list(b))
                b.clear()
        else:
            e,f,g = map(int, line.split())
            dest = [e, e+g-1]
            source = [f, f+g-1]
            b.append((source, dest))
    if b:
        b.sort()
        a.append(list(b))
        b.clear()

    return a

def pop_interval(intervals, delval):
    popped = []

    for i in range(len(intervals)-1, -1, -1):
        startinside = delval[1] >= intervals[i][0] >= delval[0]
        endinside = delval[1] >= intervals[i][1] >= delval[0]
        submerged = (intervals[i][1] >= delval[0] >= intervals[i][0]) and (intervals[i][1] >= delval[1] >= intervals[i][0])

        if submerged:
            ii = intervals.pop(i)
            if ii[0] < delval[0]-1:
                intervals.append([ii[0], delval[0]-1])
            if delval[1]+1 < ii[1]:
                intervals.append([delval[1]+1, ii[1]])
            popped.append(delval.copy())
        elif startinside and endinside:
            popped.append(intervals.pop(i))
        elif endinside:
            popped.append([delval[0], intervals[i][1]])
            intervals[i][1] = delval[0]-1
        elif startinside:
            popped.append([intervals[i][0], delval[1]])
            intervals[i][0] = delval[1]+1
    
    return popped


lines = list(map(lambda x: x.strip(), open('input', 'r').readlines()))
seeds = list(map(int, lines[0].split(':')[1].split()))
# print(list(seeds))
conversions = extract_conversions(lines[1:])

# t = 9 + 7
# for x in conversions:
#     t += len(x)
# print(t)
intervals = [ [seeds[i], seeds[i]+seeds[i+1]] for i in range(0, len(seeds), 2)]

for i in range(len(conversions)):
    tmp = []
    for j in range(len(conversions[i])):
        source, dest = conversions[i][j]
        popped = pop_interval(intervals, source)
        for interval in popped:
            diff1 = interval[0]-source[0]
            diff2 = interval[1]-source[0]
            tmp.append([dest[0]+diff1, dest[0]+diff2])
    intervals.extend(tmp)

intervals.sort()
best = min(intervals)[0]
print(best)

