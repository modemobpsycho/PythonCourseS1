from math import *

x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
q = pow(x1 - x2, 2)
w = pow(y1 - y2, 2)
p = sqrt(q + w)
print(p)
