def main(construction, schematics, i, j, c):
    if (j==len(schematics) and c>0) or (j<len(schematics) and schematics[j] < c):
        return 0
    if len(construction) == i:
        a = j == len(schematics)-1 and c == schematics[j]
        b = c == 0 and j == len(schematics)
        return 1 if a or b else 0
    if construction[i] == '#':
        return main(construction, schematics, i+1, j, c+1)
    if construction[i] == '.':
        if c > 0:
            if j<len(schematics) and schematics[j] == c:
                return main(construction, schematics, i+1, j+1, 0)
            return 0
        else:
            return main(construction, schematics, i+1, j, 0)
    total = main(construction, schematics, i+1, j, c+1)
    if c > 0:
        if j<len(schematics) and schematics[j] == c:
            total += main(construction, schematics, i+1, j+1, 0)
    else:
        total += main(construction, schematics, i+1, j, 0)
    return total

lines = list(map(lambda x: x.strip(), open('input', 'r').readlines()))
alltotal = 0
for line in lines:
    construction, schematics = line.split()
    schematics = list(map(int, schematics.split(',')))*5
    construction = '?'.join([construction]*5)
    alltotal += main(construction, schematics, 0, 0, 0)
print(alltotal)