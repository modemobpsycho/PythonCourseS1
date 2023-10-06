numbers = input().split(".")
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
counter = 0
for i in range(len(numbers)):
    if numbers[i] <= 255:
        counter += 1
if counter == 4:
    print("ДА")
else:
    print("НЕТ")

#------->>>>>

numbers = input().split(".")

for el in numbers:
    if not (0 <= int(el) <= 255):
        print("НЕТ")
        break
else:
    print("ДА")