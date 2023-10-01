a = len(input())  # Проверка на существование арифм. прогрессии из длин строк
b = len(input())
c = len(input())
if (2 * b - c - a) * (2 * c - b - a) * (2 * a - b - c) == 0:
    print("YES")
else:
    print("NO")
