counter = 0

num = int(input())
for i in range(num):
    if i % 2 == 0:
        counter += i + 1
    else:
        counter -= i + 1
print(counter)


#с оптимизацией
n = int(input())

f = 0
for i in range(1, n + 1):
    f += (-1) ** (i + 1) * i 
print(f)