from collections import defaultdict

def next_random(secret):
    mod = 16777216
    secret = (secret ^ (secret*64))%mod
    secret = ((secret//32)^secret)%mod
    secret = (((secret*2048)^secret)%mod)
    return secret


with open('input22.txt', 'r') as file:
    lines = file.readlines()

prices = defaultdict(int)

for line in lines:
    diffs = []
    prev = int(line)
    seen = set()

    for i in range(4):
        nxt = next_random(prev)
        diffs.append(nxt%10-prev%10)
        prev = nxt
    
    for i in range(2000-3):
        tdiffs = tuple(diffs)

        if not tdiffs in seen:
            seen.add(tdiffs)
            prices[tdiffs] += prev%10

        nxt = next_random(prev)
        diffs.append(nxt%10-prev%10)
        diffs.pop(0)
        prev = nxt

print(max(prices.values()))
        

