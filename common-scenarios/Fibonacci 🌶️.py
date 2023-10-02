n = int(input())
f = 0
f1 = 1
for i in range(0, n):
    f, f1 = f1, f + f1
    print(f, end=" ")