def calc_diff(seq):
    return [seq[i+1]-seq[i] for i in range(len(seq)-1)]

def all_zero(arr):
    for x in arr:
        if x != 0:
            return False
    return True

lines = list(map(lambda x: x.strip(), open('input', 'r').readlines()))
total = 0
for line in lines:
    first_diff = list(map(int, line.split()))
    all_diffs = [first_diff]
    while not all_zero(all_diffs[-1]):
        all_diffs.append(calc_diff(all_diffs[-1]))

    prev_diff = 0
    for i in range(len(all_diffs)-2, -1, -1):
        prev_diff = all_diffs[i][0] - prev_diff
    
    total += prev_diff

print(total)