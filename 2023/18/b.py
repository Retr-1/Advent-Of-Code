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

def get_instruction(hex_code:str):
   # if hex_code.startswith('#'):
   #    hex_code = hex_code[1:]
   
   instrct = ['R','D','L','U']
   i = instrct[int(hex_code[-1])]
   n = int(hex_code[:5], base=16)
   return i, n


lines = list(map(lambda x: x.strip(), open('input', 'r').readlines()))
edging = []
DIRECTIONS = {
   'L': [-1, 0],
   'R': [1, 0],
   'U': [0, -1],
   'D': [0, 1]
}

instructions = []

for i in range(len(lines)):
   a, b, color = lines[i].split()
   # instructions.append([a,b])
   # continue
   color = color[2:-1]
   heading, count = get_instruction(color)
   instructions.append([heading, count])


# print(min(instructions, key=lambda x: x[1]))
# print(max(instructions, key=lambda x: x[1]))
   
cube_count = 0
x = y = 0.5
for i in range(len(instructions)):
   curr_heading, count = instructions[i]
   # next_heading = instructions[(i+1)%len(instructions)][0]
   cube_count += count

   # V = 1
   # if curr_heading == 'R':
   #    if next_heading == 'U':
   #       x -= V
   #    elif next_heading == 'D':
   #       x += V
   # elif curr_heading == 'L':
   #    if next_heading == 'U':
   #       x += V
   #    elif next_heading == 'D':
   #       x -= V
   # elif curr_heading == 'U':
   #    if next_heading == 'L':
   #       y += V
   #    elif next_heading == 'R':
   #       y -= V
   # elif curr_heading == 'D':
   #    if next_heading == 'L':
   #       y -= V
   #    elif next_heading == 'R':
   #       y += V
   
   """
   Ked zacneme v strede tych kociek a vytvorime obal, tak dostaneme dobru aproximaciu
   Problem je, ze nie vsetkym okrajovym blokom je zobrata presne polovica obsahu, niektorym iba stvrtina inym tri stvrtiny
   Podla mojej hypotezy, kedze ideme do loopy tak sa tieto navzajom odcitaju az nakoniec zostanu iba tie, co sa 
   """

   dx, dy = DIRECTIONS[curr_heading]
   x += count*dx
   y += count*dy
   edging.append((x,y))


#952408144115
print(solve(edging) + cube_count*.5 + 1)
# print(solve([[0,0], [1,0], [2,0], [3,0], [3,1], [2,1], [1,1], [0,1]]))