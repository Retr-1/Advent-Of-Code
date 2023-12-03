def readfromfile(path):
    with open(path,'r') as f:
        line = f.readline()
        while line != '':
            line = line.removesuffix('\n')
            yield line
            line = f.readline()



events = [
    [1,0,2],
    [2,1,0],
    [0,2,1]
]
enemy = 65
player = 88
s = 0
for val in readfromfile('input2'):
    a,b = val.split()
    player_id = ord(b)-player
    enemy_id = ord(a)-enemy
    s += player_id+1 + events[player_id][enemy_id]*3

print(s)
