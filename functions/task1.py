# объявление функции
def draw_box():
    print("*" * 10)
    for _ in range(12):
        print("*", "*", sep=" "*8)
    print("*" * 10)

# основная программа
draw_box()  # вызов функции