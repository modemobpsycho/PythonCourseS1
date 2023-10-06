seq = input().split()

for el in seq:
    print("+" * int(el))
    
    

numbers = input().split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
for i in range(len(numbers)):
    print(numbers[i] * "+", sep="\n")
