res = set()
n = 203
for i in range(n + 1):
    s = '1' * i + '2' + '1' * (n - i)
    while '111' in s or '222' in s:
        if '111' in s:
            s = s.replace('111', '22', 1)
        else:
            s = s.replace('222', '11', 1)
    res.add(s)
print(max(res, key=len))
print(res)