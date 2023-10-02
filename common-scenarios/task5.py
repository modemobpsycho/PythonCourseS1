#factorial

total = 1
n = int(input())
for i in range(1, n + 1):
    total *= i
print(total)



from math import factorial
print(factorial(int(input())))



fact = lambda n: 1 if n == 0 else n * fact(n - 1)
print(fact(int(input())))