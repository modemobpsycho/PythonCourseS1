#с if
m = int(input())
n = int(input())
if m > n:
    for _ in range(n, m + 1):
        if m % 2 == 1:
            print(m)
        m = m - 1


#без if
m, n = int(input()), int(input())

start = ((m - 1) // 2) * 2 + 1

for i in range(start, n - 1, -2):
    print(i)