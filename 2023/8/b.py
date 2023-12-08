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

current = []
for x in graph:
    if x.endswith('A'):
        current.append(x)
i = 0

while True:
    for x in instructions:
        for y in current:
            if not y[2] == 'Z': break
        else:
            print(i)
            exit()

        mv = 1 if x == 'R' else 0

        for j in range(len(current)):
            current[j] = graph[current[j]][mv]

        i += 1

