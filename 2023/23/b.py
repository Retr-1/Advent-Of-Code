from sys import setrecursionlimit
setrecursionlimit(10**8)
from collections import defaultdict

class Node:
    def __init__(self) -> None:
        self.children = []
        self.edges = []
        self.end = False
    
    def add_child(self, child, traversed):
        self.children.append(child)
        self.edges.append(traversed)


lines = list(map(lambda x: x.strip(), open('input', 'r').readlines()))
W,H = len(lines[0]), len(lines)
start = (1,0)
end = (W-2, H-1)
root = Node()

# batch = [(*start,)]
# visited = [[False]*W for i in range(H)]
# while len(batch) > 0:
#     x, y, parent, traversed, visited = batch.pop(0)
#     walls = 0
#     to_explore = []
#     for nx,ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
#         if not (W > nx >= 0 and H > ny >= 0):
#             continue
#         if lines[ny][nx] == '#':
#             walls += 1
#         if visited[ny][nx]:
#             continue
#         to_explore.append((nx,ny))

#     if walls < 2:
#         conjunction = Node()
#         parent.add_child(conjunction, traversed)
#         for a,b in to_explore:
#             visited[b][a] = True
#             batch.append((a, b, conjunction, 0, visited))

# Find conjunctions
conjunctions = set()
for x in range(W):
    for y in range(H):
        if lines[y][x] == '#':
            continue

        walls = 0
        for nx,ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if not (W > nx >= 0 and H > ny >= 0):
                continue
            if lines[ny][nx] == '#':
                walls += 1
        
        if walls < 2:
            conjunctions.add((x,y))

conjunctions.add(start)
conjunctions.add(end)

# Make BFS from each conjunction, until it hits another conjunction
def binpos(x, y):
    return 1 << (W*y+x)

adj = defaultdict(list)

for sx,sy in conjunctions:
    batch = [(sx,sy,0,0)]
    while len(batch) > 0:
        x,y,visited,count = batch.pop(0)

        for nx,ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if not (W > nx >= 0 and H > ny >= 0) or lines[ny][nx] == '#' or binpos(nx, ny) & visited:
                continue
            
            if (nx,ny) == (sx,sy):
                continue

            if (nx,ny) in conjunctions:
                adj[(nx,ny)].append((x,y,visited,count))
                adj[(sx,sy)].append((nx,ny,visited,count))
                continue

            bp = binpos(nx, ny)
            new_visited = visited | bp
            batch.append((nx, ny, new_visited, count+1))
            


def bruteforce(x, y, visited, visited_conjunctions:set):
    if (x,y) == end:
        return 0
    
    if (x,y) in visited_conjunctions:
        return float('-inf')
    
    visited_conjunctions.add((x,y))
    neighbors = adj[(x,y)]
    best = float('-inf')
    for nx,ny,to_visit,count in neighbors:
        # if visited & to_visit != 0:
        #     continue

        best = max(best, bruteforce(nx, ny, 0, visited_conjunctions) + count)

    visited_conjunctions.remove((x,y))
    return best+1

print(bruteforce(start[0], start[1], 0, set()))

    