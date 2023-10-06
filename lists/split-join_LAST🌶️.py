numbers = input().split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
counter = 0
for i in range(len(numbers)):
    a = numbers[i]
    for j in range(i + 1, len(numbers)):
        if a == numbers[j]:
            counter += 1
print(counter)

#----->>>>>>

num, count = input().split(), 0

for i in range(len(num)):
    for j in range(i + 1, len(num)):
        if num[i] == num[j]:
            count += 1
            
            
print(count)