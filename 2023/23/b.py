from sys import setrecursionlimit
setrecursionlimit(10**8)


class Node:
    def __init__(self) -> None:
        self.children = {}
        self.end = False

def simplify(x, y, visited, nodes, parent):
    if (x,y) == end:
        this = Node()
        this.end = True
        tnodes = tuple(nodes)
        parent.children[tnodes] = this
        return

    visited.append((x,y))
    walls = 0
    to_explore = []

    for nx, ny in [(x+1, y), (x-1,y), (x,y+1), (x,y-1)]:
        if not (W > nx >= 0 and H > ny >= 0) or (nx,ny) in visited:
            continue
        if lines[ny][nx] == '#':
            walls += 1
            continue
        to_explore.append((nx,ny))

    if walls == 2:
        a,b = to_explore[0]
        simplify(a, b, visited, [*nodes, (a,b)], parent)
    elif walls < 2:
        this = Node()
        tnodes = tuple(nodes)
        parent.children[tnodes] = this
        for a,b in to_explore:
            simplify(a, b, visited, [], this)



lines = list(map(lambda x: x.strip(), open('test', 'r').readlines()))
W,H = len(lines[0]), len(lines)
start = (1,0)
end = (W-2, H-1)
root = Node()
print(isacyclic(1,0,set()))
exit()

simplify(1, 0, [], [], root)
print()