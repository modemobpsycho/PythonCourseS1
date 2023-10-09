def is_prime(num):

    if num == 1:
        return False
    for j in range(2, num):
        if num % j == 0:
            return False
    return True


def get_next_prime(num):

    n = num + 1

    while not is_prime(n):
        n += 1
    return n


n = int(input())


print(get_next_prime(n))
