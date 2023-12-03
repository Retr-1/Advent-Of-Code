
symbols = {}
numbers = {}
part1 = 0
part2 = 0

with open('input', 'r') as file:
    # Store coordinates of symbols and numbers
    line_count = 0
    for line in file:
        current_num = ''
        current_idx = -1
        for char_idx, char in enumerate(line):
            if char.isdigit():
                if current_num == '':
                    current_idx = char_idx
                current_num += char
            else:
                if char not in ['.', '\n']:
                    symbols[(line_count, char_idx)] = []
                if current_num not in numbers:
                    numbers[current_num] = []
                numbers[current_num].append((line_count, current_idx))
                current_idx = -1
                current_num = ''
        line_count += 1

    # Compute part 1 and add adjacent numbers to symbols dictionary
    for number in numbers:
        for coordinate in numbers[number]:
            i = coordinate[0] - 1
            while i < coordinate[0] + 2:
                for j in range(coordinate[1] - 1, coordinate[1] + len(number) + 1):
                    if i >= 0 and j >= 0 and i < line_count and j < line_count and (i, j) in symbols:
                        part1 += int(number)
                        symbols[(i, j)].append(int(number))
                        i = coordinate[0] + 2
                        break
                i += 1

    # Compute part 2
    for i in symbols:
        if len(symbols[i]) == 2:
            part2 += symbols[i][0] * symbols[i][1]

    print('Part 1:', part1)
    print('Part 2:', part2)