def get_middle_point(x1, y1, x2, y2):
    a = (x1 + x2) / 2  
    b = (y1 + y2) / 2 
    return a, b

x_1, y_1 = int(input()), int(input())
x_2, y_2 = int(input()), int(input())

x, y = get_middle_point(x_1, y_1, x_2, y_2)
print(x, y)