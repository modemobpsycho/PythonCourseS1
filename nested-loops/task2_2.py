number = int(input())
for i in range(1, number + 1):
    for j in range(i):
        print(j + 1, end="")
        j += 1
    for k in range(i - 1, 0, -1):
        print(k, end="")
    print()
