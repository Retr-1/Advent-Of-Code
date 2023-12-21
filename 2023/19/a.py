import functools
# class Operation:
#     def __init__(self, op, var, res) -> None:
#         self.op = op
#         self.var = var
#         self.res = res

#     def fillin(self, val):
#         return eval(self.op.replace(self.var, str(val)))
    

        

def loads(string):
    string = string[1:-1]
    d = {}
    for x in string.split(','):
        a,b = x.split('=')
        d[a] = int(b)
    return d

# @functools.cache
def process(workname):
    if workname in ['A','R']:
        return workname
    
    for var,expr,res in workflows[workname]:
        if not var:
            return process(res)
        
        # print(str(variables[var]), expr, workname, var, variables[var])

        if eval(str(variables[var])+expr):
            return process(res)
        

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
            expr = expr[jdx:]
            rules_better.append((var, expr, res))
        else:
            rules_better.append((None, None, r))

    workflows[name] = rules_better


total = 0
for j in range(i+1, len(lines)):
    variables = loads(lines[j])
    valid = process('in')=='A'
    
    # print(variables, valid)
    
    if valid:
        total += sum(variables.values())

print(total)