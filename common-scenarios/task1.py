counter = 0
a, b = int(input()), int(input())
for i in range(a, b + 1):
    if i**3 % 10 in {4, 9}:
        counter += 1
print(counter)
