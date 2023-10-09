def quick_merge(n):
    numbers = list()
    for i in range(n):
        numbers += [int(i) for i in input().split()]
    return sorted(numbers)
n = int(input())
print(*quick_merge(n))