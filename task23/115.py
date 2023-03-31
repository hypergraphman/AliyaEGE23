from functools import lru_cache


@lru_cache(None)
def f(s, e, k):
    if s == e:
        return 1
    if s > e or k > 9:
        return 0
    return f(s + 1, e, k + 1) + f(s + 5, e, k + 1) + f(s * 3, e, k + 1)


print(f(1, 111, 0))