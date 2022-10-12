from itertools import permutations, product

words = set()
for word in permutations('kapkan'):
    word = ''.join(word)
    if 'kk' not in word and 'aa' not in word:
        words.add(word)
print(len(words))
print(*words, sep='\n')
