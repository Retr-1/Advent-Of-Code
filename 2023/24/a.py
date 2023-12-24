from itertools import combinations
def sign(x):
    if x < 0:
        return -1
    if x > 0:
        return 1
    return 0

# Python program to find the point of
# intersection of two lines

# Class used to used to store the X and Y
# coordinates of a point respectively
class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y


def lineLineIntersection(A, B, C, D):
    # Line AB represented as a1x + b1y = c1
    a1 = B.y - A.y
    b1 = A.x - B.x
    c1 = a1*(A.x) + b1*(A.y)

    # Line CD represented as a2x + b2y = c2
    a2 = D.y - C.y
    b2 = C.x - D.x
    c2 = a2*(C.x) + b2*(C.y)

    determinant = a1*b2 - a2*b1

    if (determinant == 0):
        # The lines are parallel. This is simplified
        # by returning a pair of FLT_MAX
        return None
    else:
        x = (b2*c1 - b1*c2)/determinant
        y = (a1*c2 - a2*c1)/determinant
        return Point(x, y)


# This code is contributed by Saurabh Jaiswal




textlines = map(lambda x: x.strip(), open('input', 'r').readlines())
lines = []
LEFT = 200000000000000
RIGHT = 400000000000000
for textline in textlines:
    a,b = textline.split('@')
    x,y,z = map(int, a.split(','))
    vx,vy,vz = map(int, b.split(','))
    lines.append(((x,y,z,vx,vy,vz)))

total = 0
for la, lb in combinations(lines, 2):
    x1,y1,z1,vx1,vy1,vz1 = la
    x2,y2,z2,vx2,vy2,vz2 = lb

    A = Point(x1,y1)
    B = Point(x1+vx1, y1+vy1)
    C = Point(x2,y2)
    D = Point(x2+vx2,y2+vy2)
    res = lineLineIntersection(A,B,C,D)
	
    if not res:
        continue
    px,py = res.x, res.y
    if RIGHT >= px >= LEFT and RIGHT >= py >= LEFT:
        if sign(px - x1) == sign(vx1) and sign(px - x2) == sign(vx2) and sign(py-y1) == sign(vy1) and sign(py-y2) == sign(vy2):
            total += 1


        

print(total)