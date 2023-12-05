# 1.
When iterating with for loop and saving changes after some separator, say space, make sure that there are none unprocessed changes at the end of iteration

*Example:2023/5/b.py*
```py
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
```

# 2.
When making a change on a list in a iteration, make sure that the change doesn't affect computations performed upon the list. Otherwise you can make a copy of said list and save the change after done iterating.

*Example: 2023/5/b.py*
```py
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
```