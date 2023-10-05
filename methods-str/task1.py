s = input()
counter = 0
for i in range(len(s)):
    if(s[i] != s[i].title()):
        counter += 1
print(counter)