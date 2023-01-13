s = open('24.txt').read()
print(s)
max_len = 1
cur_len = 1
for i in range(1, len(s)):
    c1, c2 = s[i - 1], s[i]
    if c1 != c2:
        cur_len += 1
        if cur_len > max_len:
            max_len = cur_len
    else:
        cur_len = 1
print(max_len)


# 123