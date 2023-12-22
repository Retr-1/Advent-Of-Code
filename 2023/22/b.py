def do_3d_boxes_overlap(box1, box2):
    """
    Check if two 3D boxes overlap.
    Each box is defined by a tuple of (min_corner, max_corner) coordinates.
    Coordinates are given as (x, y, z).
    """
    (x1_min, y1_min, z1_min), (x1_max, y1_max, z1_max) = box1
    (x2_min, y2_min, z2_min), (x2_max, y2_max, z2_max) = box2

    # Check if there is any overlap
    if x1_max < x2_min or x2_max < x1_min:
        return False  # No overlap in x-axis
    if y1_max < y2_min or y2_max < y1_min:
        return False  # No overlap in y-axis
    if z1_max < z2_min or z2_max < z1_min:
        return False  # No overlap in z-axis

    return True  # Boxes overlap

# Example usage
# box1 = ((1, 1, 1), (4, 4, 4))
# box2 = ((2, 2, 2), (5, 5, 5))




lines = list(map(lambda x: x.strip(), open('input', 'r').readlines()))
blocks = []
for line in lines:
    a,b = line.split('~')
    start = list(map(int, a.split(',')))
    end = list(map(int, b.split(',')))
    new_start = [min(start[0], end[0]), min(start[1], end[1]), min(start[2], end[2])]
    new_end = [max(start[0], end[0]), max(start[1], end[1]), max(start[2], end[2])]

    blocks.append((new_start, new_end))


blocks.sort(key=lambda x: x[0][2])
print()
for i in range(len(blocks)):
    curr_block = blocks[i]
    while True:
        if curr_block[0][2] == 0:
            break
        curr_block[0][2] -= 1
        curr_block[1][2] -= 1
        overlap = False
        for j in range(i-1, -1, -1):
            if do_3d_boxes_overlap(curr_block, blocks[j]):
                overlap = True
                break
        
        if overlap:
            curr_block[0][2] += 1
            curr_block[1][2] += 1
            break
        
total = 0
# for i in range(len(blocks)):
#     # curr_block = blocks[i]
#     # curr_block[0][2] -= 1
#     # curr_block[1][2] -= 1
#     suppa = True
#     for j in range(len(blocks)):
#         if i == j:
#             continue
#         curr_block = blocks[j]
#         if curr_block[0][2] == 0:
#             continue
#         curr_block[0][2] -= 1
#         curr_block[1][2] -= 1
#         overlap = False
#         for k in range(len(blocks)):
#             if k == i or k == j:
#                 continue
    
#             if do_3d_boxes_overlap(curr_block, blocks[k]):
#                 overlap = True
#                 break
#         curr_block[0][2] += 1
#         curr_block[1][2] += 1
#         if not overlap:
#             suppa = False
#             break
#     if suppa:
#         total += 1
print('Done1')
supporting = [set() for i in range(len(blocks))]
for i in range(len(blocks)):
    curr_block = blocks[i]
    curr_block[0][2] += 1
    curr_block[1][2] += 1
    for j in range(len(blocks)):
        if i == j:
            continue

        if do_3d_boxes_overlap(curr_block, blocks[j]):
            supporting[i].add(j)
    curr_block[0][2] -= 1
    curr_block[1][2] -= 1


lying_on = [set() for i in range(len(blocks))]
for i in range(len(blocks)):
    curr_block = blocks[i]
    curr_block[0][2] -= 1
    curr_block[1][2] -= 1
    for j in range(len(blocks)):
        if i == j:
            continue

        if do_3d_boxes_overlap(curr_block, blocks[j]):
            lying_on[i].add(j) # the things i lies on
    curr_block[0][2] += 1
    curr_block[1][2] += 1
print('Done2')

def disintegrate(v, removed):
    t = 0
    removed.add(v)
    for x in supporting[v] - removed:
        if len(lying_on[x] - removed) == 0:
            t += disintegrate(x, removed) + 1
    return t

# rm = set()
for i in range(len(blocks)):
    # if i were to be disintegrated
    total += disintegrate(i, set())

# print(lying_on)
# print(supporting)

print(total)
# while True:
#     static = True

#     for i in range(len(blocks)):
#         curr_block = blocks[i]
#         if curr_block[0][2] == 0:
#             continue
#         curr_block[0][2] -= 1
#         curr_block[1][2] -= 1
#         overlap = False
#         for j in range(len(blocks)):
#             if i == j:
#                 continue
#             if do_3d_boxes_overlap(curr_block, blocks[j]):
#                 overlap = True
#                 break
#         if overlap:
#             curr_block[0][2] += 1
#             curr_block[1][2] += 1
#         else:
#             static = False
    
#     if static:
#         break


        





