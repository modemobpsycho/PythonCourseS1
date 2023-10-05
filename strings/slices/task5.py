from math import ceil

s = input()
print(s[len(s) - len(s) // 2 : len(s)], s[: len(s) - len(s) // 2], sep="")

#------>>>>>

s = input()
n = len(s)

a = s[:(n + 1) // 2]
b = s[(n + 1) // 2:]

print(b + a)