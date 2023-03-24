from functools import lru_cache


@lru_cache(None)
def f(n):
    if n <= 3:
        return n
    if n % 2 == 0:
        return n + f(n - 1)
    return n * n + f(n - 2)


k = 0
for i in range(1, 100000):
    if f(i) < 10**8:
        k += 1
print(k)