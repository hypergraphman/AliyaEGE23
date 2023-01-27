from functools import lru_cache


@lru_cache
def divs(n):
    d = {1, n}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return sorted(filter(lambda x: x % 2 == 0, d))


def n(k):
    num = 1_850_000_000 + k
    if len(divs(num)) % 2:
        return len(divs(num))
    return -1


k = 1
count = 0
while count < 5:
    if n(k) != -1:
        print(k, n(k))
        count += 1
    k += 1


