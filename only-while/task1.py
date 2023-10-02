s = input()
counter = 0
sl_stop = ["стоп", "хватит", "достаточно"]
while s not in sl_stop:
    counter += 1
    s = input()
print(counter)



counter = 0
while input() not in ("стоп", "хватит", "достаточно"):
    counter += 1
print(counter)
