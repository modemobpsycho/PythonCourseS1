def h(n, x, y):
    if n == 1:
        print(1, x, y)
    else:
        h(n-1, x, 6-x-y)
        print(n, x, y)
        h(n-1, 6-x-y, y)
 
n = 2
h(n, 1, 3)