from itertools import permutations, product

words = set()
for word in permutations('улей'):
    word = ''.join(word)
    if 'еу' not in word and word[0] != 'й':
        words.add(word)
print(len(words))
print(*words, sep='\n')