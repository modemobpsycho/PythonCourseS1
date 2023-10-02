#Дано натуральное число n, (n≥10). Напишите программу, которая определяет его максимальную и минимальную цифры.

n = int(input())
max_digit = 0
min_digit = 9

while n > 0:
    cur_digit = n % 10
    
    max_digit = max(max_digit, cur_digit)
    min_digit = min(min_digit, cur_digit)
    
    n //= 10
    
print("Максимальная цифра равна", max_digit)
print("Минимальная цифра равна", min_digit)