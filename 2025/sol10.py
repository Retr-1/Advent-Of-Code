from gaussian_elimination import gaussian_elimination

def solve(line: str):
    joltages = {}
    buttons = []
    nth_button = 0
    targets = None
    for x in line.split():
        if x.startswith('['):
            continue

        numbers = tuple(map(int, x.replace(x[0], '').replace(x[-1], '').split(',')))
        if x.startswith('('):
            buttons.append(numbers)
            for y in numbers:
                joltages[y] = joltages.get(y, set()) | {nth_button}
            nth_button += 1
        else:
            targets = numbers



    nrows = len(targets)    
    A = [[] for i in range(nrows)]
    for button in buttons:
        for row in range(nrows):
            A[row].append(1 if row in button else 0)

    for x in A:
        print(x)


    part, free = gaussian_elimination(A, targets)
    n_free = len(free)

    # print(part)
    # print(*free)
    # print('---')

    # print(joltages)
    # print(buttons)
    # print(targets)

    # 11 -2s

    def recursive(used_free:set):
        for idx, free in enumerate(free):
            if idx in used_free:
                continue


    
    


result = 0
with open('input2510e') as f:
    for line in f.readlines():
        result += solve(line)
        print(result)
        break
        

print(result)