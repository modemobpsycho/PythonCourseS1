number = int(input())

count_3 = 0
last_digit = number % 10
count_last_digit = 0
count_even_digits = 0
sum_greater_than_5 = 0
product_greater_than_7 = 1
count_0_5 = 0


while number > 0:
    cur_digit = number % 10

    if cur_digit == 3:
        count_3 += 1
    if cur_digit == last_digit:
        count_last_digit += 1
    if cur_digit % 2 == 0:
        count_even_digits += 1
    if cur_digit > 5:
        sum_greater_than_5 += cur_digit
    if cur_digit > 7:
        product_greater_than_7 *= cur_digit
    if cur_digit == 0 or cur_digit == 5:
        count_0_5 += 1

    number //= 10


print(count_3)
print(count_last_digit)
print(count_even_digits)
print(sum_greater_than_5)
print(product_greater_than_7)
print(count_0_5)