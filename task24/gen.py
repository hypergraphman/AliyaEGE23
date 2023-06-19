from string import ascii_uppercase
from random import choice
f = open('24gen.txt', 'w')
for i in range(10**6):
    f.write(choice(ascii_uppercase))