m, p, n = float(input()), float(input()), int(input())
[print(i + 1, m * (1 + p / 100) ** (i)) for i in range(n)]
