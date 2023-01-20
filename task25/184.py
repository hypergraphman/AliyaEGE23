def divs(n):
    d = {1, n}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return sorted(d)

cnt = 0
i = 300000001
while cnt < 5:
    t = divs(i)
    if len(t) >= 7:
        p = 1
        for el in t[1:6]:
            p *= el
        if p < i and p % 100 == 31:
            print(p, t[5])
            cnt += 1
    i += 1