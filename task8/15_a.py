from  itertools import *
number = 0
for i in product('АКРУ', repeat=5):
    number += 1
    print(number, i)