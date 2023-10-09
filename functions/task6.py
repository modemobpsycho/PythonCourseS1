# объявление функции
def get_factors(num):
    arr_digits = []
    for i in range(1, num + 1):
        if num % i == 0:
            arr_digits.append(i)
    return arr_digits

# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))