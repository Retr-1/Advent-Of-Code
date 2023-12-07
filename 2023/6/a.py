lines = list(map(lambda x: x.strip(), open('inputb', 'r').readlines()))
times = list(map(int, lines[0].split(':')[1].split()))
distances = list(map(int, lines[1].split(':')[1].split()))

g = 1
for i in range(len(times)):
    c = 0
    t = times[i]
    d = distances[i]
    for hold in range(1,t):
        if d/hold + hold <= t:
            c += 1
    g *= c

print(g)


