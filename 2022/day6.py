with open('input6','r') as f:
    string = f.read()
    string.removesuffix('\n')

packet = []
for s,x in enumerate(string):
    if x in packet:
        i = packet.index(x)
        packet[:i+1] = []
    
    packet.append(x)

    if len(packet) == 14:
        print(s+1)
        break