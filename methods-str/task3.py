n = int(input())
count = 0
for _ in range(n):
    s = input()
    if s.count("11") >= 3:
        count += 1
        continue
print(count)
