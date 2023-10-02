#Дано натуральное число. Напишите программу, которая меняет порядок цифр числа на обратный.

number = int(input())
s = " "
while number != 0:
    s = s + str(number % 10)
    number //= 10
print(int(s))


#>.<
print(input()[::-1])