def f(st, fin):
    if st == 25:
        return 0
    if st == fin:
        return 1
    if st > fin:
        return 0
    return f(st + 1, fin) + f(st * 2, fin)


print(f(2, 14) * f(14, 29))