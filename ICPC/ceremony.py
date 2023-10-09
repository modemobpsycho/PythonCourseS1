arr_all = []
arr_win = []
n_all = int(input())
for _ in range(n_all):
    el = input()
    arr_all.append(el)

n_win = int(input())
for _ in range(n_win):
    el = input()
    arr_win.append(el)

arr_attendW = []

for el in arr_win:
    checkForName = el in arr_all
    checkForReverse = " ".join((el.split(' ')[::-1])) in arr_all
    checkForRepeat = el not in arr_attendW and " ".join((el.split(' ')[::-1])) not in arr_attendW
    if (checkForName or checkForReverse) and checkForRepeat:
        arr_attendW.append(el)
        print("Applause")
    elif checkForRepeat != True:
        print("Laughter")
    else:
        print("Noise")
