ans = 'YES'
for _ in range (10):
    if int(input()) % 2:
        ans = 'NO'
        break
print(ans)



flag = True
for _ in range(10):
    n = int(input())

    if n % 2 == 1:
        flag = False

if flag:
    print('YES')
else:
    print('NO')