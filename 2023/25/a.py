from collections import defaultdict
from sys import setrecursionlimit
setrecursionlimit(10**6)

def get_size(vertex:str, visited:set):
    if vertex in visited:
        return 0
    
    total = 1
    visited.add(vertex)
    for v in neighbors[vertex]:
        total += get_size(v, visited)
    return total


def traverse(vertex:str, visited:dict, covisited:set, parent=''):
    global idx

    if vertex in visited:
        return [visited[vertex]]

    covisited.add(vertex)
    visited[vertex] = idx
    idx += 1    
    contacted = [] if parent=='' else [visited[parent]]
    for neighbor in neighbors[vertex]:
        contacted.extend(traverse(neighbor, visited, covisited))
    covisited.remove(vertex)

    t = 0
    for x in contacted:
        if x < visited[vertex]:
            t += 1
    
    if t == 3:
        # Found articulation
        subsize = get_size(vertex, covisited)
        totalsize = get_size(start, set())
        print(subsize * (totalsize-subsize))
        exit()

    # print(t)

    return contacted


lines = list(map(lambda x: x.strip(), open('input', 'r').readlines()))
neighbors = defaultdict(set)

for line in lines:
    a,b = line.split(':')
    values = b.strip().split()
    key = a.strip()
    neighbors[key].update(values)
    for v in values:
        neighbors[v].add(key)

start = key
idx = 0
traverse(start, {}, set())
# print(get_size(start, set()))