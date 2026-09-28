import random

variables = {}
rules = []
inv_rules = {}
task_variables = {}

with open('input.txt', 'r') as file:
    for line in file:
        if line == '\n':
            break
        name, value = line.split(': ')
        task_variables[name] = int(value)
    for line in file:
        a,b,c,_,d = line.split()
        inv_rules[d] = tuple(sorted((a,c)))
        rules.append((a,b,c,d))

def evaluate(variables):
# print(rules)
    changed = True
    while changed:
        changed = False

        for inp1,operator,inp2,out in rules:
            if not out in variables and inp1 in variables and inp2 in variables:
                if operator == 'AND':
                    variables[out] = variables[inp1] & variables[inp2]
                elif operator == 'OR':
                    variables[out] = variables[inp1] | variables[inp2]
                elif operator == 'XOR':
                    variables[out] = variables[inp1] ^ variables[inp2]

                changed = True

def main():
    meanies = {}

    def follow(gate):
        if gate[0] == 'x' or gate[0] == 'y':
            return
        
        if gate in meanies:
            meanies[gate] += 1
        else:
            meanies[gate] = 1
        
        inp1, inp2 = inv_rules[gate]
        follow(inp1)
        follow(inp2)

    def one_test():
        x = random.randint(0, 2**45-1)
        y = random.randint(0, 2**45-1)
        variables = {}
        for i in range(45):
            variables[f'x{i:02}'] = (1 << i) & x
        for i in range(45):
            variables[f'y{i:02}'] = (1 << i) & y
        evaluate(variables)
        exp_res = x+y
        for i in range(46):
            if (1<<i)&exp_res != variables[f'z{i:02}']:
                follow(f'z{i:02}')
    
    for i in range(10**3):
        one_test()

    return sorted(meanies.items(), key=lambda x: x[1], reverse=True)

res = main()
print(res, len(res))
res = sorted(map(lambda x: x[0], res[:8]))
print(','.join(res))

