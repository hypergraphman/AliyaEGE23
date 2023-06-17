def divs(n):
    r = {1, n}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            r.add(i)
            r.add(n // i)
    return sorted(r)


for n in range(100):
    s = 117 + 4*n
    if len(divs(s)) == 2:
        print(n)