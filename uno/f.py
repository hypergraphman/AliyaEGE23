def f(n):
    if n == 2 or n == 1:
        return 1
    return f(n - f(n - 1)) + f(n - f(n - 2))


for i in range(1, 35):
    print(f(i) % 4)