from itertools import product

for i, word in enumerate(product('AKRU', repeat=5), start=1):
    if i == 721:
        print(word)