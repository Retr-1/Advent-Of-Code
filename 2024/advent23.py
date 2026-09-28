from collections import defaultdict
from itertools import combinations



conns = {}

with open('input23_24.txt', 'r') as file:
    for line in file:
        a,b = sorted(line.strip().split('-'))
        if a in conns:
            conns[a].append(b)
        else:
            conns[a] = [b]
        
        if b in conns:
            conns[b].append(a)
        else:
            conns[b] = [a]


def is_fully_connected(points):
    for p1 in points:
        for p2 in points:
            if p1 == p2:
                continue
            
            if not p1 in conns:
                return False
            
            if not p2 in conns[p1]:
                return False
            
    return True


# print(list(combinations([1,2,3], 1)))

best = []

for key in conns:
    fuckoff = False
    for i in range(len(conns[key]), len(best)-1, -1):
        for comb in combinations(conns[key], i):
            p = (key, *comb)
            if is_fully_connected(p):
                best = p
                fuckoff = True
                break
        
        if fuckoff:
            break

print(','.join(sorted(best)))


# partys = []

# for a in conns:
#     for b in conns[a]:
#         if not b in conns:
#             continue

#         for c in conns[b]:
#             if c in conns[a]:
#                 partys.append((a,b,c))

# # print(partys)
# c = 0
# for party in partys:
#     ok = False
#     for x in party:
#         if x[0] == 't':
#             ok = True
#             break
#     c += ok
# print(c)