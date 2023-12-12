from math import factorial

def cr_when_empty(length, segments):
    free = length - (sum(segments) + len(segments)-1)
    if free < 0:
        return 0
    separators = len(segments)
    return factorial(free+separators)//(factorial(free)*factorial(separators))

def main(construction, schematics):
    i = 0
    start = [0]*len(schematics)
    start[0] = 1
    end = [0]*(len(schematics)+1)

    while i < len(construction):
        if construction[i] == '?':
            j = i+1
            while j < len(construction) and construction[j] == '?':
                j += 1
            span = j - i
            if i > 0 and construction[i-1] == '#':
                span -= 1
            for s in range(len(schematics)):
                if start[s] == 0:
                    continue
                for e in range(s+1, len(schematics)+1):
                    cr = cr_when_empty(span, schematics[s:e])
                    if cr != 0:
                        if end[e] != 0:
                            end[e] *= start[s] * cr
                        else:
                            end[e] = start[s] * cr
            start = end
            start[0] = 1
            end = [0]*(1+len(schematics))
            i = j
        elif construction[i] == '#':
            j = i+1
            while j < len(construction) and construction[j] == '#':
                j += 1
            span = j - i
            for k in range(len(schematics)):
                if schematics[k] == span:
                    end[k+1] = start[k]
            start = end
            end = [0]*(1+len(schematics))
            i = j
        else:
            i += 1

    return start[len(schematics)]            


lines = list(map(lambda x: x.strip(), open('test', 'r').readlines()))
alltotal = 0
for line in lines:
    construction, schematics = line.split()
    schematics = list(map(int, schematics.split(',')))*5
    construction = '?'.join([construction]*5)
    alltotal += main(construction, schematics)
    break
    
print(alltotal)