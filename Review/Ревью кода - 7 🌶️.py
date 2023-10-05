n = input()
s = 0
while n > 10:
    if n % 2 == 1:
        s = n % 10
    n //= 10
print(s)

#----->>>>

n = int(input())
s = 0
while n > 0:
    if n % 2 == 0:
        s += n % 10
    n //= 10
print(s)