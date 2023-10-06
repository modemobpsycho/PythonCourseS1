n = int(input())
seq = []

for _ in range(n):
    cur = int(input())
    seq.append(cur)

del seq[1::2]
    
print(seq)