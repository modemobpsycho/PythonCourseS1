#Дано натуральное число. Напишите программу, которая вычисляет: сумму его цифр; количество цифр в нем; произведение его цифр; 
#среднее арифметическое его цифр; его первую цифру; сумму его первой и последней цифры.

number = int(input())
number_cop = number
total_d = 1
sum_d = 0
counter = 0
last_digit = number_cop % 10
while number != 0:
    sum_d += number % 10
    counter += 1
    total_d *= number % 10

    first_digit = number % 10
    number //= 10

print(sum_d)
print(counter)
print(total_d)
print(sum_d / counter)

print(first_digit)
print(first_digit + last_digit)


#with lib
import numpy
nums = [int(i) for i in input()]
print(sum(nums), len(nums), numpy.prod(nums), numpy.mean(nums), nums[0], nums[0] + nums[-1], sep='\n')