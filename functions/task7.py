# объявление функции
def number_of_factors(num):
    # объявление функции
    arr_digits = []
    for i in range(1, num + 1):
        if num % i == 0:
            arr_digits.append(i)
    return len(arr_digits)

# считываем данные
n = int(input())

# вызываем функцию
print(number_of_factors(n))