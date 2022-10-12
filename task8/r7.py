from itertools import permutations, product

words = set()
for word in product('весна', repeat=3):
# for word in permutations():
    word = ''.join(word)
    if 'а' in word:
        words.add(word)
print(len(words))
print(*words, sep='\n')
