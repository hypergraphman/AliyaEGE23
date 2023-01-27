from functools import lru_cache


@lru_cache
def divs(n):
    d = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return sorted(filter(lambda x: x % 2 == 0, d))


def d(k):
    num = 100_000_000 - k
    if len(divs(num)) >= 5 and divs(num)[-5]:
        return len(divs(num))
    return -1


k = 1
count = 0
while count < 5:
    if d(k) != -1:
        print(divs(100_000_000 - k)[-5], d(k), 100_000_000 - k)
        count += 1
    k += 1


