import math

def solve(current):
    i = 0
    while True:
        for x in instructions:
            if current[2] == 'Z':
                return i

            mv = 1 if x == 'R' else 0
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


print(math.lcm())