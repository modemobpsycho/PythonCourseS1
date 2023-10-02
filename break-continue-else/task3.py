num = int(input())
n = num
flag = False
while n != 0:
    last = n % 10
    if last == 7:
        flag = True
        break        # прерываем цикл, так как число гарантированно содержит цифру 7
    n //= 10

if flag is True:
    print('Число', num, 'содержит цифру 7')
else:
    print('Число', num, 'не содержит цифру 7')
    
#not same things

num = int(input())
n = num
while n != 0:
    last = n % 10
    if last == 7:
        print('Число', num, 'содержит цифру 7')
        break
    n //= 10
else:
    print('Число', num, 'не содержит цифру 7')