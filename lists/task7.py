negative = []
positive = []
zero = []
n = int(input())
for i in range(n):
    numbers = int(input())
    if numbers < 0:
        negative.append(numbers)
    elif numbers == 0:
        zero.append(numbers)
    else:
        positive.append(numbers)
print(*negative, sep ="\n")
print(*zero, sep ="\n")
print(*positive, sep ="\n")



negatives, zeros, positives = [], [], []

n = int(input())
for _ in range(n):
    cur = int(input())
    if cur < 0:
        negatives.append(cur)
    elif cur > 0:
        positives.append(cur)
    else:
        zeros.append(cur)
        
res = negatives + zeros + positives
print(*res, sep="\n")