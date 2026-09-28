def solve(line: str):
    # namiesto setov používame integer bitmasky
    # bit i == button i
    joltages = {}
    buttons = []
    nth_button = 0
    targets = None

    for x in line.split():
        if x.startswith('['):
            continue

        numbers = tuple(
            map(
                int,
                x.replace(x[0], '').replace(x[-1], '').split(',')
            )
        )

        if x.startswith('('):
            buttons.append(numbers)

            button_bit = 1 << nth_button

            for y in numbers:
                # pôvodne:
                # joltages[y] = joltages.get(y, set()) | {nth_button}

                joltages[y] = joltages.get(y, 0) | button_bit

            nth_button += 1

        else:
            targets = numbers

    best = float('inf')

    # aby sme nemuseli stále volať len(buttons[idx])
    button_sizes = [len(button) for button in buttons]

    def recursive(stats, used_buttons, k, stats_sum):
        nonlocal best

        # toto ostáva
        if any(x < 0 for x in stats):
            return

        # pôvodne:
        # if sum(stats) == 0:
        if stats_sum == 0:
            best = min(best, k)
            return

        # pôvodne:
        # if len(used_buttons) == len(buttons):
        if used_buttons.bit_count() == len(buttons):
            return

        if best < k:
            return

        def apply_button(button_idx, count):
            for v in buttons[button_idx]:
                stats[v] += count

        def process(button_idx, count):
            # nemusíme meniť used_buttons tam a späť
            new_used_buttons = used_buttons | (1 << button_idx)

            apply_button(button_idx, -count)

            # aplikácia buttonu count-krát zníži sumu o:
            # count * počet jeho togglov
            recursive(
                stats,
                new_used_buttons,
                k + count,
                stats_sum - count * button_sizes[button_idx]
            )

            apply_button(button_idx, count)

        # ----------------------------------------------------------
        # nájdi joltage, ktorý môže ovplyvniť už iba jeden button
        # ----------------------------------------------------------

        for jolt in joltages:
            # pôvodne:
            #
            # remaining = joltages[jolt] - used_buttons
            #
            # teraz je to jediná bitová operácia

            remaining = joltages[jolt] & ~used_buttons

            if remaining == 0:
                if stats[jolt] != 0:
                    return

            # presne jeden nastavený bit
            elif remaining & (remaining - 1) == 0:
                # index jediného zostávajúceho buttonu
                chosen_idx = remaining.bit_length() - 1

                count = stats[jolt]

                process(chosen_idx, count)
                return

        # ----------------------------------------------------------
        # nájdi button s minimálnym počtom možností
        # ----------------------------------------------------------

        best_mx = float('inf')
        best_idx = None

        for idx, button in enumerate(buttons):
            # pôvodne:
            # if idx in used_buttons:

            if used_buttons & (1 << idx):
                continue

            mx = float('inf')

            for button_toggle in button:
                mx = min(mx, stats[button_toggle])

            if mx < best_mx:
                best_mx = mx
                best_idx = idx

        for g in range(best_mx + 1):
            process(best_idx, g)

    print(joltages)
    print(buttons)

    stats = list(targets)

    recursive(
        stats,
        0,              # prázdny used_buttons
        0,
        sum(stats)
    )

    return best


result = 0

with open('input2510') as f:
    for line in f:
        result += solve(line)
        print(result)

print(result)