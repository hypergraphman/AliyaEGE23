for x in range(15):
    s1 = 15 ** 4 + 2 * 15 ** 3 + 3 * 15 ** 2 + x * 15 + 5
    s2 = 15 ** 4 + x * 15 ** 3 + 2 * 15 ** 2 + 3 * 15 + 3
    if (s1 + s2) % 14 == 0:
        print((s1 + s2) // 14, x)
