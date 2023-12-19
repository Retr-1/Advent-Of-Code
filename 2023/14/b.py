
def shift_north(lines):
    out = [ ['']*w for i in range(h) ]
    for x in range(len(lines[0])):
        i = 0
        for y in range(len(lines)):
            if lines[y][x] == 'O':
                out[i][x] = 'O'
                i += 1
            elif lines[y][x] == '#':
                i = y+1
                out[y][x] = '#'
    return out



def rotate_matrix_90_degrees_clockwise(matrix):
    new_matrix = []
    for i in range(len(matrix[0])):
        li = list(map(lambda x: x[i], matrix))
        li.reverse()
        new_matrix.append(li)

    return new_matrix

def count(lines):
    total = 0
    for x in range(w):
        for y in range(h):
            if lines[y][x] == 'O':
                total += h-y
    return total
    

def main(cycles, lines):
    table = lines
    history = [tuple(map(tuple, lines))]

    for i in range(1,cycles):
        for k in range(4):
            table = shift_north(table)
            table = rotate_matrix_90_degrees_clockwise(table)
        
        fixed = tuple(map(tuple, table))

        # for x in table:
        #     print(''.join([y if y!='' else '.' for y in x]))

        # print()
        
        if fixed in history:
            j = history.index(fixed)
            p = i - j
            remaining = (cycles - j) % p         
            end_table = history[remaining + j]
            print(p, j)

            # for x in history:
            #     print(count(x))

            return count(end_table)
        
        # if count(fixed) < 100:
        #     print(count(fixed))
        history.append(fixed)


lines = list(map(lambda x: x.strip(), open('input', 'r').readlines()))
h = len(lines)
w = len(lines[0])

print(main(1000000000, lines))
# for x in rotate_matrix_90_degrees_clockwise([
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]):
#     print(x)
# 1 1 2 2 2 3 3 3 4 4 4 5 5