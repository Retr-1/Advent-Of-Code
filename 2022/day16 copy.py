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

memo = {}
memo2 = {}
# def main(vertex, elevertex, finish, elefinish, bitmask,time):       
#     if time >= 26:
#         return 0

#     if time == finish:
#         stamp = 1
#         best = 0
#         score = rates[vertex]*(26-time-1)
#         for i in range(len(valves)):
#             if stamp & bitmask:
#                 best = max(best, main(valves[i], elevertex, time+dist[vertex][valves[i]]+1, elefinish, bitmask^stamp, min(elefinish, time+dist[vertex][valves[i]]+1)))
#             stamp *= 2
#         return score + best

#     elif time == elefinish:
#         stamp = 1
#         best = 0
#         score = rates[elevertex]*(26-time-1)
#         for i in range(len(valves)):
#             if stamp & bitmask:
#                 best = max(best, main(vertex, valves[i], finish, time+dist[elevertex][valves[i]]+1, bitmask^stamp, min(finish, time+dist[elevertex][valves[i]]+1)))
#             stamp *= 2
#         return score + best

def main(vertex,bitmask,time):       
    if time >= 26:
        return 0

    if bitmask == 0:
        return rates[vertex]*(26-time-1)

    if (vertex,bitmask,time) in memo:
        return memo[(vertex,bitmask,time)]

    stamp = 1
    best = 0
    score = rates[vertex]*(26-time-1)
    for i in range(len(valves)):
        if stamp & bitmask:
            best = max(best, main(valves[i], bitmask^stamp, time+dist[vertex][valves[i]]+1))
        stamp *= 2
    
    score += best
    memo[(vertex,bitmask,time)] = score
    return score

def extended_main(vertex,bitmask,time):      
    if time >= 26:
        return 0

    if bitmask == 0:
        return rates[vertex]*(26-time-1)

    if (vertex,bitmask,time) in memo2:
        return memo2[(vertex,bitmask,time)]

    stamp = 1
    best_total = float('-inf')
    for i in range(len(valves)):
        if bitmask & stamp:
            best_total = max(best_total, main(valves[i],bitmask^stamp, dist['AA'][valves[i]]))
        stamp *= 2
        #print(best)

    stamp = 1
    best = 0
    score = rates[vertex]*(26-time-1)
    for i in range(len(valves)):
        if stamp & bitmask:
            best = max(best, extended_main(valves[i], bitmask^stamp, time+dist[vertex][valves[i]]+1))
        stamp *= 2

    best += score
    best_total += score

    memo2[(vertex,bitmask,time)] = max(best,best_total)
    return max(best,best_total)



best = float('-inf')
for i in range(len(valves)):
    best = max(best, extended_main(valves[i],beginmask^(2**i), dist['AA'][valves[i]]))
    #print(best)
print(best)
