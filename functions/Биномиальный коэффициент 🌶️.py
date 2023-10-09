from math import factorial as f

def compute_binom(n, k):
    return f(n) // (f(k) * f(n - k))

n = int(input())
k = int(input())

print(compute_binom(n, k))