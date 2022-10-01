def n_to_p(n, p):
    res = ''
    alf = '0123456789ABCDEFGHIJKLM'
    while n > 0:
        d = n % p
        res = alf[d] + res
        n //= p
    return res


print(n_to_p(194, 16))
print(int('1234', 5))