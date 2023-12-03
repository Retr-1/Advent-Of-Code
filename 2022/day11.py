from mycode import readfromfile
from typing import NamedTuple


class Monkey():
    items: list
    operation: str
    test: int
    yes: int
    no: int
    inspects: int

    def __init__(self,items,operation,test,yes,no) -> None:
        self.items = items
        self.operation = operation
        self.test = test
        self.yes = yes
        self.no = no
        self.inspects = 0

    def getworry(self,item):
        return eval(self.operation.replace('old',str(item)))


monkeys = []

intel = readfromfile('input11')
for line in intel:
    if line.startswith('Monkey'):
        items = list(map(lambda x: int(x), next(intel).split(':')[1].split(',')))
        operation = next(intel).split(':')[1].split('=')[1]
        test = next(intel)
        test = int(test[test.find('by')+2:].strip())
        yes = int(next(intel).split()[-1])
        no = int(next(intel).split()[-1])

        monkeys.append(Monkey(items,operation,test,yes,no))

MOD = 1
for monkey in monkeys:
    MOD *= monkey.test

# MOD = 10**9-7

for i in range(10000):
    #print(i)
    for monkey in monkeys:
        monkey.inspects += len(monkey.items)
        for item in monkey.items:
            worry = monkey.getworry(item)%MOD
            if worry%monkey.test == 0:
                monkeys[monkey.yes].items.append(worry)
            else:
                monkeys[monkey.no].items.append(worry)
        monkey.items = []

monkeys.sort(key=lambda x: x.inspects, reverse=True)
print(monkeys)
print(monkeys[0].inspects*monkeys[1].inspects)