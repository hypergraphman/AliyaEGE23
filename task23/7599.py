def f(s, e, p):
    if s > e or s == 13:
        return 0
    if s == e:
        if 'aa' not in p:
            print(p)
            return 1
        else:
            return 0
    return f(s + 1, e, p + 'a') + f(s + 2, e, p + 'b') + f(s * 3, e, p + 'c')


print(f(3, 18, ''))