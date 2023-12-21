def loads(string):
    string = string[1:-1]
    d = {}
    for x in string.split(','):
        a,b = x.split('=')
        d[a] = int(b)
    return d

def process(workname, intervals):
    if workname in ['A','R']:
        if workname == 'A':
            accepted.append(intervals)
        return
    
    
    for var,val,op,res in workflows[workname]:

        if not var:
            new_intervals = intervals.copy()
            return process(res, new_intervals)
        
        if op == '<': # x < val
            new_intervals = intervals.copy()
            new_intervals[var] = (new_intervals[var][0], min(new_intervals[var][1], val))
            if new_intervals[var][1]-new_intervals[var][0]-1 > 0:
                process(res, new_intervals)
            intervals[var] = (max(intervals[var][0], val-1), intervals[var][1])
            
        elif op == '>': # x > val
            new_intervals = intervals.copy()
            new_intervals[var] = (max(new_intervals[var][0], val), new_intervals[var][1])
            if new_intervals[var][1]-new_intervals[var][0]-1 > 0:
                process(res, new_intervals)
            intervals[var] = (intervals[var][0], min(val+1, intervals[var][1]))


def unify(intervals):
    intervals.sort()
    new_intervals = []
    curr_interval = intervals.pop(0)
    for x in intervals:
        if curr_interval[1] < x[0]:
            new_intervals.append(curr_interval)
            curr_interval = x
            continue
        curr_interval = (curr_interval[0], max(curr_interval[1], x[1]))
    new_intervals.append(curr_interval)
    return new_intervals

        

lines = list(map(lambda x: x.strip(), open('input', 'r').readlines()))
workflows = {}

for i in range(len(lines)):
    if lines[i] == '':
        break
    idx = lines[i].find('{')
    name = lines[i][:idx]
    rules = lines[i][idx+1:-1].split(',')
    rules_better = []
    for r in rules:
        if ':' in r:
            expr, res = r.split(':')
            jdx = max(expr.find('<'), expr.find('>'))
            var = expr[:jdx]
            val = int(expr[jdx+1:])
            op = expr[jdx]
            rules_better.append((var, val, op, res))
        else:
            rules_better.append((None, None,None, r))

    workflows[name] = rules_better

total = 0
accepted = []
process('in', {'x':(0,4001), 'm':(0,4001), 'a':(0,4001), 's':(0,4001)})
# for x in ['x','m','a','s']:
#     print(unify([accepted[i][x] for i in range(len(accepted))]))
total = 0
for x in accepted:
    s = 1
    for key in x:
        s *= x[key][1]-x[key][0]-1
    total += s
print(total)
