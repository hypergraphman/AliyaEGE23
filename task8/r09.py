from itertools import permutations, product

words = set()
for word in permutations('вуаль'):
    word = ''.join(word)
    if 'ьа' not in word and 'ьу' not in word and word[0] != 'ь':
        words.add(word)
print(len(words))
print(*words, sep='\n')
