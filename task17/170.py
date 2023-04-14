*a, = map(int, open('17-4.txt'))
res = []
for el in a:
    if el % 13 == 4 and el % 8 == 1:
        res.append(el)
print(max(res), sum(res))