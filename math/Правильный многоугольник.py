from math import pow, tan, pi

n, a = int(input()), float(input())
res = n * pow(a, 2) / (4 * tan(pi / n))

print(res)
