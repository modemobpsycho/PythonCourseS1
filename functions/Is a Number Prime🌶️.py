# объявление функции
def is_prime(num):
    if num == 1:  
        return False
    for j in range(2, num):
        if num % j == 0:  
            return False
    return True          

# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))