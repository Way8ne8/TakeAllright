import itertools


def primes():
    a = 2
    while True:  # просто пример
        b = False
        for i in range(2, a):
            if a % i == 0:
                b = True
        if b == False:
            yield a
        a += 1



print(list(itertools.takewhile(lambda x: x <= 31, primes())))
