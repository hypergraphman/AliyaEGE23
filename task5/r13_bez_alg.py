for i in range(2, 100):
    n = i
    s1 = f'{n:b}'
    s2a = s1 + str(sum(map(int, s1)) % 2)
    s2b = s2a + str(sum(map(int, s2a)) % 2)
    int(s2b, 2)
    if int(s2b, 2) > 77:
        print(i)
        break