from collections import defaultdict

lines = list(map(lambda x: x.strip().split(), open('input', 'r')))

strengths = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
strengths.reverse()

FULL_HOUSE = 4
FOUR_OF_KIND = 5
FIVE_OF_KIND = 6
THREE_OF_KIND = 3
TWO_PAIR = 2
ONE_PAIR = 1
HIGH_CARD = 0

def get_score(hand):
    things = defaultdict(int)

    for x in hand:
        things[x] += 1

    items = sorted(things.values(), reverse=True)

    if items[0] == 3:
        if len(items) == 2:
            return FULL_HOUSE
        return THREE_OF_KIND
    
    if items[0] == 5:
        return FIVE_OF_KIND
    
    if items[0] == 4:
        return FOUR_OF_KIND
    
    if items[0] == 2:
        if items[1] == 2:
            return TWO_PAIR
        return ONE_PAIR
    
    if items[0] == 1:
        return HIGH_CARD
    
    assert True

def get_hand_priority(hand):
    return [strengths.index(x) for x in hand]


hands = []

for line in lines:
    hand, bid = line
    bid = int(bid)

    hands.append((get_score(hand), get_hand_priority(hand), bid))

hands.sort()
total = 0
for i in range(len(hands)):
    total += hands[i][2]*(i+1)

print(total)


    
