import numpy as np

def block_extractor(lines):
    curr = []
    for line in lines:
        if line == '\n':
            yield curr
            curr.clear()
        else:
            curr.append(line.strip())

row = col = 0
for ll in block_extractor(open('input', 'r').readlines()):
    lines = np.array(list(map(lambda x: list(x), ll)))
    # print(lines)

    for i in range(lines.shape[1]-1):
        minlen = min(i+1, lines.shape[1]-i-1)
        left = lines[:, i-minlen+1: i+1]
        right = np.fliplr(lines[:, i+1: i+minlen+1])
        # print(i)
        # print( i-minlen+1, i+1)
        # print( i+1,  i+minlen+1)
        # print(left)
        # print(right)
        # print()
        if np.array_equal(left, right):
            col += i+1
            

    for j in range(lines.shape[0]-1):
        minlen = min(j+1, lines.shape[0]-j-1)
        left = lines[j-minlen+1: j+1, :]
        right = np.flipud(lines[j+1: j+minlen+1, :])

        if np.array_equal(left, right):
            row += j+1
            

print(col + row*100)

# 0 1 2 3 4
# 1 2  