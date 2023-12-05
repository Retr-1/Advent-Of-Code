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
            dest = [e, e+g]
            source = [f, f+g]
            b.append((source, dest))
    if b:
        b.sort()
        a.append(list(b))
        b.clear()

    return a

def pop_interval(intervals, delval):
    grabbed = [float('inf'), float('-inf')]

    for i in range(len(intervals)-1, -1, -1):
        startinside = delval[1] > intervals[i][0] > delval[0]
        endinside = delval[1] > intervals[i][1] > delval[0]

        if startinside and endinside:
            grabbed[0] = min(grabbed[0], intervals[i][0])
            grabbed[1] = max(grabbed[1], intervals[i][1])
            intervals.pop(i)
            continue
        elif endinside:
            grabbed[0] = min(grabbed[0], delval[0])
            grabbed[1] = max(grabbed[1], intervals[i][1])
            intervals[i][1] = delval[0]
        elif startinside:
            grabbed[0] = min(grabbed[0], intervals[i][0])
            grabbed[1] = max(grabbed[1], delval[1])
            intervals[i][0] = delval[1]
        
        if intervals[i][0] == intervals[i][1]:
            intervals.pop(i)

    return grabbed


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
    for j in range(len(conversions[i])):
        source, dest = conversions[i][j]
        popped = pop_interval(intervals, source)
        if popped[0] == float('inf'):
            continue
        diff1 = popped[0]-source[0]
        diff2 = popped[1]-source[0]
        intervals.append([dest[0]+diff1, dest[0]+diff2])

intervals.sort()
best = min(intervals)[0]
print(best)

