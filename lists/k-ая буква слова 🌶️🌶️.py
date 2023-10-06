n = int(input())
cloud = []
string = " "
for _ in range(n):
    n = input()
    cloud.append(n)
k = int(input())
for i in range(len(cloud)):
    m = cloud[i]
    if k <= len(m):
        x = m[k - 1]
        string += x
print(string)
