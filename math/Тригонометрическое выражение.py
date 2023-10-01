from math import sin, cos, tan, radians

angle = radians(float(input()))
res = sin(angle) + cos(angle) + tan(angle) ** 2
print(res)
