import timeit
import random


def fast_pow(base, degree, module):
    degree = bin(degree)[2:]
    r = 1

    for i in range(len(degree) - 1, -1, -1):
        r = (r * base ** int(degree[i])) % module
        base = (base ** 2) % module
    return r


def test_Rabin_Miller(n, k):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False

    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    print('d = {0}'.format(d))
    print('s = {0}'.format(r))
    print('---'*20)

    for i in range(k):
        a = random.randint(2, int(n/2))
        x = pow(a, d, n)
        print('a = {0}'.format(a))
        print('x = {0}'.format(x))

        if x == 1 or x == n - 1:
            continue

        for j in range(1, r):
            x = fast_pow(x, 2, n)
            #if x != 0:print('x = {0}'.format(x))
            if x == 1:return False
            if x == n - 1:return True
        return False
    return True


n, k = int(input("Введите n: ")), int(input("Введите k: "))
result = test_Rabin_Miller(n, k)

if result == True:
    print("Число {0} вероятно простое".format(n))
else:
    print("Число {0} составное".format(n))