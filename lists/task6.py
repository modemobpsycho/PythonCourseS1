n = int(input())

strings = []
for _ in range(n):
    s = input()
    strings.append(s)
    
search_query = input()
for s in strings:
    if search_query.lower() in s.lower():
        print(s)