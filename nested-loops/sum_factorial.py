from math import factorial

number = int(input())
summ_fact = 0
for i in range(1, number + 1):
    summ_fact += factorial(i)
print(summ_fact)



n, total = int(input()), 0
for i in range(1, n + 1):
    multip = 1
    for j in range(1, i + 1):
        multip *= j
    total += multip
print(total)