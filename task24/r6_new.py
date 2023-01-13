s = open('k8-0.txt').read()
a = [s[0]]
cur_len = 1
max_len = 1
for i in range(1, len(s)):
    c1, c2 = s[i - 1], s[i]
    if c1 == c2:
        cur_len += 1
        if cur_len > max_len:
            max_len = cur_len
            a = [c2]
        elif cur_len == max_len:
            a.append(c2)
    else:
        cur_len = 1
print(max_len, a)
