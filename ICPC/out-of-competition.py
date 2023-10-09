from math import ceil

def round_digit(num1, num2):
    x = (num1 * num2) / 100
    return(round(x))

s = input()
values = s.split()
num1 = int(values[0])
num2 = int(values[1])
print(round_digit(num1, num2))