#Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.

number = input()
if(max(number) == min(number)):
    print("YES")
else:
    print("NO")
    
    
    
n = int(input())
flag = "YES"
last_digit = n % 10

while n > 0:
    cur_digit = n % 10
    
    if last_digit != cur_digit:
        flag = "NO"

    n //= 10

print(flag)