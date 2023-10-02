#Дано натуральное число n(n>9). Напишите программу, которая определяет его вторую (с начала) цифру.

import numpy
nums = [int(i) for i in input()]
print(nums[1])



n = int(input())
while n > 99:
    n //= 10

second_digit = n % 10
print(second_digit)