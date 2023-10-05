s = input("Напиши текст ")
s1 = s

x = ''
for i in range (len(s)):
    x += str(ord(s[i])) + " "
print(f"В Unicode будет выглядеть так: {x}")
s2 = x
z = ""
print("*"*24)
text = ""
textfinal = ""
counter = int(x[:x.find(" ")])
while x:
    print(counter, end="")
    while counter:
        text += str(counter%2)
        counter //= 2

    text = text[::-1]
    textfinal += text
    print(" в двоичном коде будет выглядеть так:", text)
    text = ""
    x = x[x.find(" "):]
    x = x.lstrip()
    if len(x)<= 1:
        print("Цифр не осталось!")
    if len(x) >= 1:
        counter = int(x[:x.find(" ")])
    textfinal += " "
s3 = text
print("*"*24)
print(f"Текст = {s1}", f"В Unicode = {s2}",  f"В двоичном = {textfinal}", sep="\n")
print("*"*24)