#Дано натуральное число. Напишите программу, которая определяет, является ли последовательность его цифр при просмотре справа
#налево упорядоченной по неубыванию.

number = int(input())
flag = True
last_digit = number % 10
while number > 0:
    if last_digit > number % 10:
        flag = False
    last_digit = number % 10
    number //= 10
if flag:
    print("YES")
else:
    print("NO")
