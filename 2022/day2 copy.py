def readfromfile(path):
    with open(path,'r') as f:
        line = f.readline()
        while line != '':
            line = line.removesuffix('\n')
            yield line
            line = f.readline()



events = [
    [2,0,1],
    [0,1,2],
    [1,2,0]
]
enemy = 65
player = 88
s = 0
for val in readfromfile('input2'):
    a,b = val.split()
    enemy_choice = ord(a)-enemy
    outcome = ord(b)-player
    s += events[enemy_choice][outcome]+1 + outcome*3

print(s)
