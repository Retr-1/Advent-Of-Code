import math

def solve(current):
    i = 0
    history = []
    timestamps = []
    while True:
        for j in range(len(instructions)):
            if current[2] == 'Z':
                key = (current, j)
                if key in history:
                    index = history.index(key)
                    nonperidic = history[:index]
                    periodic = history[index:]
                    period = i - timestamps[index]
                    start = timestamps[index]
                    return nonperidic, periodic, period, start
                history.append(key)
                timestamps.append(i)

            mv = 1 if instructions[j] == 'R' else 0
            current = graph[current][mv]
            i += 1

lines = list(map(lambda x: x.strip(), open('input', 'r').readlines()))
instructions = lines[0]
graph = {}
for line in lines[2:]:
    a,b = line.split('=')
    a = a.strip()
    l,r = b.strip().replace('(', '').replace(')', '').split(',')
    l = l.strip()
    r = r.strip()
    graph[a] = (l,r)

everything = []
for x in graph:
    if x.endswith('A'):
        everything.append(x)


data = [solve(x) for x in everything]
print(math.lcm(*map(lambda x: x[2], data)))