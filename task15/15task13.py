for a in range(100):
    is_a = True
    for x in range(100):
        for y in range(100):
            k = x ** 2 - 10 * x + 16 > 0
            l = y ** 2 - 10 * y + 21 > 0
            m = x * y < 2 * a
            if not(k or l or m):
                is_a = False
    if is_a:
        print(a)