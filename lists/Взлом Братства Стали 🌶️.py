n = input()  

for _ in range(int(n[1:])):
    s = input()              
    if '#' in s:             
        s = s[:s.find('#')] 
    print(s.rstrip())
