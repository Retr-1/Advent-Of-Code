def da_hash(string):
    total = 0
    for x in string:
        total += ord(x)
        total *= 17
        total %= 256
    return total

line = open('input','r').readline().strip()
values = line.split(',')

print(sum(map(da_hash, values)))
print(da_hash('qp'))