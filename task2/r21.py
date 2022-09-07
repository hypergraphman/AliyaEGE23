from itertools import product

print('x y z w')
for x, y, z, w in product((0, 1), repeat=4):
    f = int(((x and not y) or (w <= z)) == (z == x))
    if f:
        print(x, y, z, w)
