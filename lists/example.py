num = int(input())
arr = []
for i in range(97, num + 97):
    s = list(chr(i))
    arr += s
print(arr)
