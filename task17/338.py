data = list(map(int, open('17-338.txt').readlines()))

mn = min(data)
mx = 0
k = 0
for i in range(1, len(data)):
    el1, el2 = data[i - 1], data[i]
    if el1 % 117 == mn or el2 % 117 == mn:
        k += 1
        mx = max(mx, el1 + el2)
print(k, mx)
