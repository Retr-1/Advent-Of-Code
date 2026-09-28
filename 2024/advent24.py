import random


rules = {}

with open('input.txt', 'r') as file:
    for line in file:
        if line == '\n':
            break

    for line in file:
        a,b,c,_,d = line.split()
        rules[(a,b,c)] = d
        # rules[(c,b,a)] = d




# def construct(gate):
#     if gate[0] == 'x' or gate[0] == 'y':
#         return gate, int(gate[1:])
    
#     inp1,operation,inp2 = inv_rules[gate]
#     eq1, p1 = construct(inp1)
#     eq2, p2 = construct(inp2)
#     if p1 > p2:
#         return f'({eq1}{operation}{eq2})', p1
#     return f'({eq2}{operation}{eq1})', p2

# # print(construct('z09'))

# myrules = {}
# myrules[('x00', 'XOR', 'y00')] = 'z00'
# myrules[('x00', 'AND', 'y00')] = 'carry0'
# for i in range(1,45):
#     # value
#     myrules[(f'x{i:02}', 'XOR', f'y{i:02}')] = f'a{i}'
#     myrules[(f'a{i}', 'XOR', f'carry{i-1}')] = f'z{i:02}'

#     # carry
#     myrules[(f'x{i:02}', 'AND', f'y{i:02}')] = f'b{i}'
#     myrules[(f'a{i}', 'AND', f'carry{i-1}')] = f'c{i}'
#     myrules[(f'b{i}', 'OR', f'c{i}')] = f'carry{i}'

# print(myrules)
# print(len(myrules), len(rules))




swapped = []

def swap_wires(wire1, wire2):
    global rules
    swapped.append(wire1)
    swapped.append(wire2)

    new_rules = {}

    for rule in rules:
        x = rules[rule]

        if rule[0] == wire1:
            rule = (wire2, rule[1], rule[2])
        if rule[2] == wire1:
            rule = (rule[0], rule[1], wire2)
        if rule[0] == wire2:
            rule = (wire1, rule[1], rule[2])
        if rule[2] == wire2:
            rule = (rule[0], rule[1], wire1)

        if x == wire1:
            x = wire2
        elif x == wire2:
            x = wire1
        
        new_rules[rule] = x

    
    rules = new_rules


def get_wire(key):
    if key in rules:
        return rules[key]
    if (key[2], key[1], key[0]) in rules:
        return rules[(key[2], key[1], key[0])]
    
    for rule in rules:
        if rule[1] != key[1]:
            continue
            
        if key[0] == rule[0]:
            swap_wires(key[2], rule[2])
            return get_wire(key)
        elif key[0] == rule[2]:
            swap_wires(key[2], rule[0])
            return get_wire(key)
        elif key[2] == rule[0]:
            swap_wires(key[0], rule[2])
            return get_wire(key)
        elif key[2] == rule[2]:
            swap_wires(key[0], rule[0])
            return get_wire(key)

carry_wire = get_wire(('x00', 'AND', 'y00'))

for i in range(1, 45):
    # value
    a = get_wire((f'x{i:02}', 'XOR', f'y{i:02}'))

    w = get_wire((a, 'XOR', carry_wire))
    if not w == f'z{i:02}':
        swap_wires(w, f'z{i:02}')

    # carry
    c = get_wire((f'x{i:02}', 'AND', f'y{i:02}'))
    d = get_wire((a, 'AND', carry_wire))
    e = get_wire((c, 'OR', d))
    carry_wire = e
    

if carry_wire != 'z45':
    swap_wires(carry_wire, 'z45')

print(','.join(sorted(swapped)))
    


