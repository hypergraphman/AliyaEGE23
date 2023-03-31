def f(s, e):
    if s > e or s == 21:
        return 0
    if s == e:
        return 1
    return f(s + 1, e) + f(s + 4, e) + f(s + s + 2 - s % 2, e)


print(f(2, 11) * f(11, 21))