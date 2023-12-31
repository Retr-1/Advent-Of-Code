from math import ceil

def getInfo(x1, y1, x2, y2):
   return x1*y2 - y1*x2

def solve(points):
   N = len(points)
   firstx, firsty = points[0]
   prevx, prevy = firstx, firsty
   res = 0

   for i in range(1, N):
      nextx, nexty = points[i]
      res = res + getInfo(prevx,prevy,nextx,nexty)
      prevx = nextx
      prevy = nexty
   res = res + getInfo(prevx,prevy,firstx,firsty)
   return abs(res)/2.0


lines = list(map(lambda x: x.strip(), open('input', 'r').readlines()))
edging = []
x = y = 0.5
DIRECTIONS = {
    'L': [-1, 0],
    'R': [1, 0],
    'U': [0, -1],
    'D': [0, 1]
}
for i in range(len(lines)):
    heading, count, color = lines[i].split()
    dx, dy = DIRECTIONS[heading]
    for j in range(int(count)):
        x += dx
        y += dy
        edging.append((x,y))

print(ceil(solve(edging) + .5*len(edging) + 1))
# print(solve([[0,0], [1,0], [2,0], [3,0], [3,1], [2,1], [1,1], [0,1]]))