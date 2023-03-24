def f(n):
    print(n)
    if n > 0:
        d = n % 10 + f(n // 10)
        print(d)
        return d
    else:
        return 0


i = 1
while sum(map(int, str(i))) <= 32:
    i += 1
print(i)
f(i)