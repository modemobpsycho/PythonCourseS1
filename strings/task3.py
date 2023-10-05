s = input()
cnt_plus = 0
cnt_mul = 0

for el in s:
    if el == "+":
        cnt_plus += 1
    elif el == "*":
        cnt_mul += 1

print("Символ + встречается", cnt_plus, "раз")
print("Символ * встречается", cnt_mul, "раз")