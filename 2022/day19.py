from math import ceil
from mycode import readfromfile, extractdigit

blueprints = []
intel = readfromfile('input19')
for line in intel:
    line = line.split('.')
    l = line[0]
    a = extractdigit(l,l.find('costs')+6)
    l = line[1]
    b = extractdigit(l,l.find('costs')+6)
    l = line[2]
    c = extractdigit(l,l.find('costs')+6), extractdigit(l,l.find('and')+4)
    l = line[3]
    d = extractdigit(l,l.find('costs')+6), extractdigit(l,l.find('and')+4)
    blueprints.append((a,b,c,d))

print(len(blueprints))

memo = {}

def main(time,robots,minerals,blueprint):
    def new_minerals(t,ore=0,clay=0,obsidian=0,geode=0):
        return (minerals[0]+ore+robots[0]*t, minerals[1]+clay+robots[1]*t, minerals[2]+obsidian+robots[2]*t, minerals[3]+geode+robots[3]*t)

    def new_robots(ore=0,clay=0,obsidian=0,geode=0):
        return (robots[0]+ore,robots[1]+clay,robots[2]+obsidian,robots[3]+geode)

    if time > 24:
        return 0

    if time==24:
        #print(robots,minerals)
        return minerals[3]

    # if (time,robots,minerals) in memo:
    #     return memo[(time,robots,minerals)]

    best = (24-time)*robots[3] + minerals[3]

    if max(blueprint[0],blueprint[1],blueprint[2][0],blueprint[3][0]) > robots[0]:
        if blueprint[0] <= minerals[0]:
            best = max(best,main(time+1, new_robots(ore=1), new_minerals(1,ore=-blueprint[0]),blueprint))
        else:
            timeout = ceil((blueprint[0]-minerals[0])/robots[0]) + 1
            best = max(best,main(time+timeout, new_robots(ore=1), new_minerals(timeout,ore=-blueprint[0]),blueprint))
    
    if (blueprint[3][1]-robots[2])*blueprint[2][1] > (blueprint[3][1]-robots[2])*robots[1]+minerals[1]: #blueprint[2][1] > robots[1] and (blueprint[3][1]-robots[2])*blueprint[2][1] > minerals[1]:
        if blueprint[1] <= minerals[0]:
            best = max(best,main(time+1, new_robots(clay=1), new_minerals(1,ore=-blueprint[1]),blueprint))
        else:
            timeout = ceil((blueprint[1]-minerals[0])/robots[0]) + 1
            best = max(best,main(time+timeout, new_robots(clay=1), new_minerals(timeout,ore=-blueprint[1]),blueprint))

    if (24-time)*blueprint[3][1] > robots[2]*(24-time)+minerals[2]:
        if blueprint[2][0] <= minerals[0] and blueprint[2][1] <= minerals[1]:
            best = max(best,main(time+1, new_robots(obsidian=1), new_minerals(1,ore=-blueprint[2][0], clay=-blueprint[2][1]),blueprint))    
        elif robots[1]:
            timeout = max(ceil((blueprint[2][0]-minerals[0])/robots[0]), ceil((blueprint[2][1]-minerals[1])/robots[1])) + 1
            best = max(best,main(time+timeout, new_robots(obsidian=1), new_minerals(timeout,ore=-blueprint[2][0], clay=-blueprint[2][1]),blueprint))

    if blueprint[3][0] <= minerals[0] and blueprint[3][1] <= minerals[2]:
        best = max(best,main(time+1, new_robots(geode=1), new_minerals(1,ore=-blueprint[3][0], obsidian=-blueprint[3][1]),blueprint))
    elif robots[2]:
        timeout = max(ceil((blueprint[3][0]-minerals[0])/robots[0]), ceil((blueprint[3][1]-minerals[2])/robots[2])) + 1
        best = max(best,main(time+timeout, new_robots(geode=1), new_minerals(timeout,ore=-blueprint[3][0], obsidian=-blueprint[3][1]),blueprint))


    #memo[(time,robots,minerals)] = best
    return best

total = 0
for i,x in enumerate(blueprints):
    #memo = {}
    total += main(0,(1,0,0,0),(0,0,0,0),x)*(i+1)
print(total)