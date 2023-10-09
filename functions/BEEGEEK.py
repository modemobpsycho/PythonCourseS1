def is_palindrome(num):
    return str(num) == str(num)[::-1]


def is_prime(num):
    if num == 1:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False  
    return True


def is_even(num):
    return num % 2 == 0


def is_valid_password(password):
    l = password.split(":")
    
    
    if len(l) == 3:  
        l = [int(el) for el in l]   
        a, b, c = l[0], l[1], l[2]       
        return is_palindrome(a) and is_prime(b) and is_even(c)
    return False 

psw = input()

print(is_valid_password(psw))