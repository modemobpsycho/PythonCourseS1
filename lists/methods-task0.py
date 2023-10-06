numbers = input().split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
ind_max = numbers.index(max(numbers))
ind_min = numbers.index(min(numbers))

numbers[ind_min], numbers[ind_max] = numbers[ind_max], numbers[ind_min]
print(*numbers, sep=" ")
