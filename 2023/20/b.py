from collections import defaultdict
from math import lcm

LOW = False
HIGH = True
NO_RESPONSE = -1

class FlipFlop:
    def __init__(self) -> None:
        self.state = LOW

    def send(self, name, signal):
        if signal == LOW:
            self.state = not self.state
            return self.state
        return NO_RESPONSE
    
class Conjunction:
    def __init__(self, ingoing=None) -> None:
        self.ingoing = {}#defaultdict(bool)
        #self.ingoing = dict(zip(ingoing, [LOW]*len(ingoing)))

    def send(self, sender, signal):
        assert sender in self.ingoing
        self.ingoing[sender] = signal
        if all(self.ingoing.values()):
            return LOW
        return HIGH

class Broadcaster:
    def send(self, name, signal):
        return signal
    

def push_the_button():
    batch = [('broadcaster', LOW, 'button')]
    while len(batch) > 0:
        name, signal, sender = batch.pop(0)

        if signal == LOW and name in conj_in:
            # print(signal, modules['lv'][0].ingoing)
            idx = conj_in.index(name)


            # conj_in_times[idx].append(signal)
            # if not conj_in_period[idx] and len(conj_in_times[idx])%2 == 0:
            #     half = len(conj_in_times[idx])//2
            #     if half > 100 and conj_in_times[idx][:half] == conj_in_times[idx][half:]:
            #         conj_in_period[idx] = half
            #         print('Period', idx, half, conj_in_times[idx])
            conj_in_times[idx].append(i)
            if len(conj_in_times[idx]) == 2:
                period = conj_in_times[idx][1]-conj_in_times[idx][0]
                conj_in_period[idx] = period

            if all(conj_in_period):
                f = 1
                for x in conj_in_period:
                    f *= x
                print(f)
                # exit()

        if not name in modules:
            continue

        obj, dest = modules[name]
        response = obj.send(sender, signal)
        if response != NO_RESPONSE:
            for x in dest:
                batch.append((x, response, name))



            
modules = {}
lines = list(map(lambda x: x.strip(), open('input', 'r').readlines()))
for line in lines:
    for x in ['%', '&', 'broadcaster']:
        if not line.startswith(x):
            continue

        a, b = line.split('->')
        name = a[len(x):].strip()
        dest = b.strip().split(', ')
        if x == '%':
            thing = FlipFlop()
        elif x == '&':
            thing = Conjunction()
        else:
            thing = Broadcaster()
            name = x
        modules[name] = [thing, dest]

for x in modules:
    o = modules[x][0]
    if type(o) != Conjunction:
        continue

    for y in modules:
        if x in modules[y][1]:
            o.ingoing[y] = False



conj_in = []
for x in modules:
    if 'lv' in modules[x][1]:
        conj_in.append(x)
conj_in_times = [[] for i in range(len(conj_in))]
conj_in_period = [None]*len(conj_in)
print(conj_in)

i = 0
while True:
    if push_the_button():
        print(i)
        break
    i += 1




"""
0,0,0,0... -> 1,0,1,0,1,0...
1,0,1,0,1,0... -> _,1,_,0,_,1,_,0


"""