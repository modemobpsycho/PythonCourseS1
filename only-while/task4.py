number = int(input())
counter = 0
while number == abs(number) and number < 6:
    if number == 5:
        counter += 1
    number = int(input())
print(counter)
