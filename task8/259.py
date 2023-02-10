from itertools import product


def check(w1, w2):
    k = 0
    for c1, c2, in zip(w1, w2):
        if c1 == c2:
            k += 1
    return k == 2


s = set()
for word in product('polykv', repeat=4):
    word = ''.join(word)
    if check(word, 'volk'):
        s.add(word)
print(len(s))