sl_r = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: "X"}
num = int(input())
if num in sl_r:
    print(sl_r[num])
else:
    print("ошибка")
