data = list(map(int, open('17-339.txt').readlines()))

mn = 10 ** 10
for el in data:
    if el > 0 and el % 19 == 0 and el < mn:
        mn = el

mx = 0
k = 0
for i in range(1, len(data)):
    el1, el2 = data[i - 1], data[i]
    if el1 + el2 < mn:
        k += 1
        mx = max(mx, el1 + el2)
print(k, abs(mx))
