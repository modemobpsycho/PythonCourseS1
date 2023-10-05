s_digits = input()
flag = False
for i in range(len(s_digits)):
    if( s_digits[i].isdigit()):
        flag = True
        break
if flag:
    print("Цифра")
else:
    print("Цифр нет")