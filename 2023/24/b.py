import sympy as sym

textlines = map(lambda x: x.strip(), open('input', 'r').readlines())
lines = []
LEFT = 200000000000000
RIGHT = 400000000000000
for textline in textlines:
    a,b = textline.split('@')
    x,y,z = map(int, a.split(','))
    vx,vy,vz = map(int, b.split(','))
    lines.append(((x,y,z,vx,vy,vz)))

"""
x + dx*t1 == x1 + dx1*t1
y + dy*t1 == y1 + dy1*t1
z + dz*t1 == z1 + dz1*t1

n points == 3n equations == n + 6 variables
3n = n+6
n = 3

If I pick 3 points it should give me precise rock parameters

I need it in form AX = B, where X are the unknowns
x + dx*t1 - x1 - dx1*t1 = 0
x + (dx-dx1)*t1 - x1 = 0
x + (dx-dx1)*t1 = x1
"""

x,y,z,dx,dy,dz = sym.symbols('x,y,z,dx,dy,dz', real=True)
equations = []
time_variables = []
for i in range(3):
    #xi,yi,zi = sym.Symbol(f'x{i},y{i},z{i}')
    x1,y1,z1,dx1,dy1,dz1 = lines[i]
    
    t1 = sym.symbols(f't{i+1}', real=True)
    time_variables.append(t1)

    a = sym.Eq(x+dx*t1, x1+dx1*t1)
    b = sym.Eq(y+dy*t1, y1+dy1*t1)
    c = sym.Eq(z+dz*t1, z1+dz1*t1)
    equations.append(a)
    equations.append(b)
    equations.append(c)

# print(len(equations), len(time_variables)+6)

result = sym.solve(equations, [x,y,z,dx,dy,dz,*time_variables], dict=True)
print(result[0][x] + result[0][y] + result[0][z])

