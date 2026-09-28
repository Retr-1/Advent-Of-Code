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

    best = float('inf')

    def recursive(stats: list, used_buttons: set, k):
        nonlocal best
        # print(len(used_buttons))
        # print(stats)

        if any(map(lambda x: x<0, stats)):
            return

        if sum(stats) == 0:
            best = min(best, k)
            # print(best)
            return

        if len(used_buttons) == len(buttons):
            return
        
        if best < k:
            return


        def apply_button(button_idx, count):
            for v in buttons[button_idx]:
                stats[v] += count


        def process(button_idx, count):
            used_buttons.add(button_idx)
            apply_button(button_idx, -count)
            recursive(stats, used_buttons, k+count)
            apply_button(button_idx, count)
            used_buttons.remove(button_idx)

        


        # find the button that needs to be used, because no other influences that joltage
        for jolt in joltages:
            remaining = joltages[jolt] - used_buttons
            if len(remaining) == 0 and stats[jolt] != 0:
                return
            
            if len(remaining) == 1:
                chosen_idx = next(iter(remaining))
                count = stats[jolt]

                return process(chosen_idx, count)

        
        # find the button with minim possibilities

        best_mx = float('inf')
        best_idx = None

        for idx, button in enumerate(buttons):
            if idx in used_buttons:
                continue

            mx = float('inf')
            for button_toggle in button:
                mx = min(mx, stats[button_toggle])

            if mx < best_mx:
                best_mx = mx
                best_idx = idx

        
        for g in range(0, best_mx+1):
            process(best_idx, g)

        


    print(joltages)
    print(buttons)
    recursive(list(targets), set(), 0)
    return best


result = 0
with open('input2510') as f:
    for line in f.readlines():
        result += solve(line)
        print(result)
        

print(result)