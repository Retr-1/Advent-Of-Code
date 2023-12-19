def da_hash(string):
    total = 0
    for x in string:
        total += ord(x)
        total *= 17
        total %= 256
    return total

line = open('input','r').readline().strip()
values = line.split(',')
boxes = [[] for i in range(256)]

for val in values:
    if '=' in val:
        box_label, focal_len = val.split('=')
        box_idx = da_hash(box_label)
        focal_len = int(focal_len)
        for i in range(len(boxes[box_idx])):
            if boxes[box_idx][i][0] == box_label:
                boxes[box_idx][i][1] = focal_len
                break
        else:
            boxes[box_idx].append([box_label, focal_len])

    elif '-' in val:
        box_label = val.removesuffix('-')
        box_idx = da_hash(box_label)
        for i in range(len(boxes[box_idx])):
            if boxes[box_idx][i][0] == box_label:
                boxes[box_idx].pop(i)
                break

total = 0

for i in range(256):
    for j in range(len(boxes[i])):
        total += (i+1)*(j+1)*boxes[i][j][1]

print(total)