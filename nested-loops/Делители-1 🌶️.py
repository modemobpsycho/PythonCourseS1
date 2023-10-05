#На вход программе подается два натуральных числа a и b (a < b). 
#Напишите программу, которая находит натуральное число из отрезка [a;b] с максимальной суммой делителей.

a = int(input())
b = int(input())
total = 0
largest = 0
for i in range(a, b + 1):
    counter = 0
    for j in range(1, i + 1):
        if i % j == 0:
            counter += j
            if counter >= total:
                total = counter
                largest = i
print(largest, total)
