from heapq import heappush,heappop

with open('input','r') as f:
    threemost = [float('-inf')]*3
    goblin = 0
    for line in f.readlines():
        line = line.removesuffix('\n')
        if line == '':
            third_goblin = heappop(threemost)
            heappush(threemost, max(third_goblin,goblin))
            goblin = 0
            continue

        goblin += int(line)

print(sum(threemost))