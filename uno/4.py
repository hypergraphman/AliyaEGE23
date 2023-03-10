for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            for d in 0, 1:
                f = a != b != c != d
                print(a, b, c, d, int(f))

