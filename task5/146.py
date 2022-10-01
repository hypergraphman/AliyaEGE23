def alg(n):
    s1 = f'{n:b}'
    s2 = s1 + s1[-1]
    # if s1.count('1') % 2 == 0:
    #     s3 = s2 + '0'
    # else:
    #     s3 = s2 + '1'
    s3 = s2 + ('0' if s1.count('1') % 2 == 0 else '1')
    # s3 = s2 + ('0', '1')[s1.count('1') % 2]
    # s4 = s3 + '0' if s3.count('1') % 2 == 0 else '1'
    if s3.count('1') % 2 == 0:
        s4 = s3 + '0'
    else:
        s4 = s3 + '1'
    return int(s4, 2)

print(alg(1))

mn = 141
for i in range(1, 200):
    t = alg(i)
    if mn > t > 130:
        mn = t
print(mn)