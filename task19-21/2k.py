win = 77
lose = 100
start = 7


def f(a, b, c, m):
    # if a < lose:
    #     return c % 2 != m % 2
    if a + b >= win:
        return c % 2 == m % 2
    if c == m:
        return False
    moves = [f(a + 1, b, c + 1, m),
             f(a * 2, b, c + 1, m),
             f(a, b + 1, c + 1, m),
             f(a, b * 2, c + 1, m)]
    return any(moves) if (c + 1) % 2 == m % 2 else all(moves)


for s in range(1, win - start):
    for m in range(1, 5):
        if f(start, s, 0, m):
            print(s, m)
            break