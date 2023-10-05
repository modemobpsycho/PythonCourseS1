number = int(input())
count = 0
for row in range(1, number + 1):
    for col in range(row):
        print(count + 1, end=' ')
        count += 1
    print()

