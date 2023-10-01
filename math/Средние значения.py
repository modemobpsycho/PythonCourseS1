import math

a = float(input())
b = float(input())

arithmetic_mean = (a + b) / 2

geometric_mean = math.sqrt(a * b)

harmonic_mean = 2 / ((1 / a) + (1 / b))

quadratic_mean = math.sqrt((a**2 + b**2) / 2)

print(arithmetic_mean)
print(geometric_mean)
print(harmonic_mean)
print(quadratic_mean)
