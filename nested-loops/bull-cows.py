for x in range(1, 101):
    for y in range(1, 101):
        for z in range(1, 101):
            if x * 10 + y * 5 + z * 0.5 == 100 and x + y + z == 100:
                print('Быков:', x, 'Коров:', y, 'Телят:', z)