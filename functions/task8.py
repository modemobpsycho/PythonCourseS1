def find_all(target, symbol):
    n = 0   
    l = []  
    for i in target:     
        if i == symbol:  
            l.append(n) 
        n += 1           
    return l             

s = input()      
char = input()   

print(find_all(s, char))