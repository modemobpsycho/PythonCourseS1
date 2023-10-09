# объявление функции
def print_fio(name, surname, patronymic):
    return surname[0].upper(), name[0].upper(), patronymic[0].upper()

# считываем данные
name, surname, patronymic = input(), input(), input()

# вызываем функцию
print(*print_fio(name, surname, patronymic), sep="")