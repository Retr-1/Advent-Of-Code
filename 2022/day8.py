from mycode import getlines

plain = getlines('input8')
plain.pop()
H = len(plain)
W = len(plain[0])
# visible = [ [False]*W for _ in range(H) ]

# mosttop = [float('-inf')]*W
# for y in range(1,H-1):
#     mostleft = float('-inf')
#     for x in range(1,W-1):
#         mosttop[x] = max(mosttop[x],int(plain[y-1][x]))
#         mostleft = max(mostleft, int(plain[y][x-1]))
#         val = int(plain[y][x])
#         if val > mostleft or val > mosttop[x]:
#             visible[y][x] = True

# out = 0
# mostdown = [float('-inf')]*W
# for y in range(H-2,0,-1):
#     mostright = float('-inf')
#     for x in range(W-2,0,-1):
#         mostdown[x] = max(mostdown[x],int(plain[y+1][x]))
#         mostright = max(mostright, int(plain[y][x+1]))
#         val = int(plain[y][x])
#         if val > mostright or val > mostdown[x] or visible[y][x]:
#             out += 1

#print(out+2*W+2*H-4)
best = 0
for y in range(1,H-2):
    for x in range(1,W-2):
        total = 1
        v = int(plain[y][x])

        score = 0
        for i in range(y-1,-1,-1):
            score += 1
            if int(plain[i][x]) >= v:
                break
        
        total *= score

        
        score = 0
        for i in range(y+1,H):
            score += 1
            if int(plain[i][x]) >= v:
                break
        
        total *= score

        
        score = 0
        for i in range(x-1,-1,-1):
            score += 1
            if int(plain[y][i]) >= v:
                break
        
        total *= score

        
        score = 0
        for i in range(x+1,W):
            score += 1
            if int(plain[y][i]) >= v:
                break
        
        total *= score

        best = max(best, total)
print(best)