def divs(n):
    d = {1, n}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return sorted(d)

for n in range(0, 100):
    if n * 3 + n * 5 + 9 >= 100 and len(divs(n * 3 + n * 5 + 9)) == 2:
        print(n * 3 + n * 5 + 9, n)
        break