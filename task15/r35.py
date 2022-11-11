for a in range(1, 1000):
    is_a = True
    for x in range(1, 1000):
        ndxa = not (x % a == 0)
        dx6 = x % 6 == 0
        ndx9 = not (x % 9 == 0)
        if not (ndxa <= (dx6 <= ndx9)):
        # if not (x % a == 0 or ((x % 6 == 0) <= (not (x % 9 == 0)))):
            is_a = False
            break
    if is_a:
        print(a)


for a in range(1, 1000):
    if all([x % a == 0 or ((x % 6 == 0) <= (not (x % 9 == 0))) for x in range(1, 1000)]):
        print(a)
