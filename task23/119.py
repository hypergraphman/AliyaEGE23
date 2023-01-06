from itertools import product


def one(x):
    return x + 1


def two(x):
    return x + 5


def three(x):
    return x * 3


s = set()
for cmds in product((one, two, three), repeat=8):
    r = 1
    for cmd in cmds:
        r = cmd(r)
    if 1000 <= r <= 1024:
        print(cmds)
        s.add(r)
print(len(s))
