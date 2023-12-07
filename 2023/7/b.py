from collections import defaultdict

lines = list(map(lambda x: x.strip().split(), open('input', 'r')))

strengths = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
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
    j = 0

    for x in hand:
        if x == 'J':
            j += 1
        else:
            things[x] += 1
            
    if j == 5:
        return FIVE_OF_KIND

    items = sorted(things.values(), reverse=True)

    if items[0]+j >= 5:
        return FIVE_OF_KIND

    if items[0]+j >= 4:
        return FOUR_OF_KIND

    if items[0]+j >= 3:
        if len(items) == 2:
            return FULL_HOUSE
        return THREE_OF_KIND
    
    if items[0]+j >= 2:
        leftover = j - (2-items[0])
        if items[1]+leftover >= 2:
            return TWO_PAIR
        return ONE_PAIR
    
    return HIGH_CARD
    

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


    
