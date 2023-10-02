from math import *

n = int(input())
num = 0
for i in range(1, n):
    num = num + (1 / (i + 1))
num2 = 1 + num - log(n)
print(num2)
