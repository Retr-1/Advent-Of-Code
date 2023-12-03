from mycode import readfromfile, extractdigit



valves = []
connections = {}
rates = {}

for line in readfromfile('input16'):
    a = line.find('Valve')
    valve = line[a+6:a+6+2]
    rate = extractdigit(line,line.find('rate')+5)
    tunnels = line[line.find('valve',line.find(';'))+6:].replace(' ','').split(',')

    connections[valve] = tunnels
    if rate > 0:
        valves.append(valve)
        rates[valve] = rate


def dijsktra(s):
    batch = [(0,s)]
    visited = {}

    while len(batch) > 0:
        cost,vertex = batch.pop(0)

        if vertex in visited:
            continue

        visited[vertex] = cost

        for nxt_vertex in connections[vertex]:
            batch.append((cost+1,nxt_vertex))

    visited[s] = 0
    return visited


def warshal():
    dists = {}
    for x in valves:
        dists[x] = dijsktra(x)
    if not 'AA' in valves:
        dists['AA'] = dijsktra('AA')
    return dists


dist = warshal()
best = float('-inf')
beginmask = 2**(len(valves))-1
# batch = [('AA',begin,0,0)]
# while len(batch) > 0:
#     valve,unvisited,time,score = batch.pop(0)
#     print(len(batch),unvisited,time,score)

#     if time >= 30:
#         best = max(best,score)
#         break

#     if unvisited != begin:
#         time += 1
#         score += (30-time)*rates[valve]
#         best = max(best, score)

#     stamp = 1
#     for i in range(len(valves)):
#         if stamp & unvisited:
#             batch.append((valves[i], unvisited^stamp, time+dist[valve][valves[i]], score))
#         stamp *= 2

memo = {}
def main(vertex,bitmask,time):       
    if time >= 30:
        return 0

    if bitmask == 0:
        return rates[vertex]*(30-time-1)

    if (vertex,bitmask,time) in memo:
        return memo[(vertex,bitmask,time)]

    stamp = 1
    best = 0
    score = rates[vertex]*(30-time-1)
    for i in range(len(valves)):
        if stamp & bitmask:
            best = max(best, main(valves[i], bitmask^stamp, time+dist[vertex][valves[i]]+1))
        stamp *= 2
    
    score += best
    memo[(vertex,bitmask,time)] = score
    return score



best = float('-inf')
for i in range(len(valves)):
    best = max(best, main(valves[i],beginmask^(2**i), dist['AA'][valves[i]]))
    #print(best)
print(best)
