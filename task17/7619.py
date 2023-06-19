*a, = map(int, open('17_7619.txt'))
res = []
mx = 0
for el in a:
    if 10 <= el < 100 and el > mx:
        mx = el
print(mx)
for i in range(len(a) - 1):
    p1, p2 = a[i], a[i + 1]
    if ((10 <= p1 < 100) != (10 <= p2 < 100)) and (p1 + p2) % mx == 0:
        res.append(p1 + p2)
print(len(res), max(res))
