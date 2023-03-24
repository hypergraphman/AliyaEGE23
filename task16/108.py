from functools import lru_cache


@lru_cache(None)
def f(n):
    if n == 0:
        return 1
    if n > 0 and n % 2 == 0:
        return f(n - 1) + f(n - 2)
    if n > 0 and n % 2 != 0:
        return 3 * f(n - 1) // 2


print(len(set(str(f(150)))))