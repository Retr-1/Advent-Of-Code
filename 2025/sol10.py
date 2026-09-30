from gaussian_elimination import gaussian_elimination
EPS = 10**-6

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

    # for x in A:
    #     print(x)


    part, free_vars = gaussian_elimination(A, targets)
    n_free = len(free_vars)
    nvars = len(buttons)

    # s <= 2+t
    # t <= 5
    # s <= 1+t
    # s >= 0
    # t <= 3
    # t >= 0
    # min: 11 - s + t
    
    status = [0] * n_free
    best = float('inf')
    UPPER_BOUND = max(targets)+1

    def recursive(idx):
        nonlocal best

        if idx == -1:
            total = sum(part)
            for i in range(n_free):
                total += sum(free_vars[i])*status[i]
            best = min(best, total)
            return
        

        minimum = 0
        maximum = UPPER_BOUND
        # check bounds
        for i in range(nvars):
            for j in range(n_free):
                if abs(free_vars[j][i]) > EPS:
                    break

            
            if j != idx or abs(free_vars[j][i]) > EPS:
                continue
            mult = -free_vars[j][i]
            total = part[i]*mult
            for k in range(j+1, n_free):
                total += free_vars[k][i]*mult*status[k]

            if mult < 0:
                minimum = max(minimum, total)
            else:
                maximum = min(maximum, total)


        initial_value = status[idx]

        for i in range(int(minimum), int(maximum)+1):
            status[idx] = i
            recursive(idx-1)

        status[idx] = initial_value

    # print(part)
    # print(*free_vars)
    # print('---')

    # print(joltages)
    # print(buttons)
    # print(targets)

    recursive(n_free-1)
    return best


    
    


result = 0
with open('input2510') as f:
    for i,line in enumerate(f.readlines()):
        # if i != 1:
        #     continue
        r = solve(line)
        print(i, r)
        result += r
        
        

print(result)