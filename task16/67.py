def f(n):
    if n < 3:
        return n + 1
    if n % 2:
        return f(n - 2) + n - 2
    return n + 2 * f(n + 2)


k = 0
for i in range(1, 1000):
    try:
        if 100 <= f(i) < 1000:
            k += 1
    except RecursionError:
        pass
print(k)