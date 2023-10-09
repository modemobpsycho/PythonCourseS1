# объявление функции
def is_password_good(password):
    if len(password) < 8:
        return False

    flagD = False 
    flagL = False 
    flagU = False
    for c in password:
        if c.isdigit():    
            flagD = True
        elif c.islower(): 
            flagL = True
        elif c.isupper():
            flagU = True

    return flagD and flagL and flagU

txt = input()

# вызываем функцию
print(is_password_good(txt))