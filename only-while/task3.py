total = 0
number = int(input())
while number == abs(number):
    total += number
    number = int(input())
print(total)
