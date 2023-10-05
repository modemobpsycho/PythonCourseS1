a = int(input())
a = format(a, 'b')
print(a)



n = int(input())
res = ""

while n > 0:
    res = str(n % 2) + res
    n //= 2

print(res)



print(f"{int(input()):b}")