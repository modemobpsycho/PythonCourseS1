n = int(input())
sp1 = []

for _ in range(n):
    s = input()
    sp1.append(s)
    
k = int(input())
sp2 = []

for _ in range(k):
    query = input()
    for i in range(len(sp1)):
        if query.lower() in sp1[i].lower() and query not in sp2:
            sp2.append(query)
            
sp3 = []
for s in sp1:
    is_matched = True
    for query in sp2:
        if query.lower() not in s.lower():
            is_matched = False
            break
    if is_matched:
        sp3.append(s)

print(*sp3, sep="\n")
