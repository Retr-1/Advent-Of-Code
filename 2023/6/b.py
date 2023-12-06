from math import ceil, floor

lines = list(map(lambda x: x.strip(), open('inputb', 'r').readlines()))
times = list(map(int, lines[0].split(':')[1].split()))
distances = list(map(int, lines[1].split(':')[1].split()))


for i in range(len(times)):
    t = times[i]
    d = distances[i]

    D = (t**2 - 4*d)**0.5
    a = ceil((t-D)/2)
    b = floor((t+D)/2)

    print(b-a+1)






