def is_palindrome(text):
    
    for c in (',.!?- '):  
        text = text.replace(c, '')
    text = text.lower()  
    return text == text[::-1] 

txt = input()

print(is_palindrome(txt))