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

current = 'AAA'
i = 0

while True:
    for x in instructions:
        if current == 'ZZZ':
            print(i)
            exit()

        mv = 1 if x == 'R' else 0
        current = graph[current][mv]
        i += 1


