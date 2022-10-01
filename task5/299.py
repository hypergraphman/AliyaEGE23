def alg(n):
    s1 = f'{n:b}'
    # if sum(map(int, s1)) % 2 == 0:
    if s1.count('1') % 2 == 0:
        s2 = s1[1:].lstrip('0')
    else:
        s2 = '1' + s1 + '00'
    if s2.count('1') % 2 == 0:
        s3 = s2[1:].lstrip('0')
    else:
        s3 = '1' + s2 + '00'
    return int(s3, 2)


i = 1
while alg(i) <= 100:
    i += 1
print(i)