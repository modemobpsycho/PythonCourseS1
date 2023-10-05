num = int(input())
for i in range(1, num + 1):
    counter = 0
    for j in range(1, i + 1):
        if i % j == 0:
            counter += 1
    print(i, "+" * counter, sep="")
