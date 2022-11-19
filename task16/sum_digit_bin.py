def f(n):
    if n == 1:
        return 5
    else:
        return n % 2 + f(n // 2)


print(f(100))
