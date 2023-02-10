c = 0
for line in open('9-170.txt').readlines():
    a = list(map(int, line.split()))
    f1 = False
    f2 = True
    for el in a:
        if a.count(el) == 2:
            f1 = True
            if f1:
                for el2 in a:
                    if a.count(el2) == 1 and el2 >= el:
                        f2 = False
    if f1 and f2:
        c += 1

print(c)
