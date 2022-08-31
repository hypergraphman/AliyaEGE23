from itertools import product

print('a b')
for a, b in product((0, 1), repeat=2):
    f = int(a and b or not a and not b)
    print(a, b, f)