with open('24-171.txt') as f:
    line = f.read()

template = 'XYZ'
cur_len = 0
max_len = 0
for char in line:
    if char == template[cur_len % len(template)]:
        cur_len += 1
        max_len = max(max_len, cur_len)
    else:
        if char == template[0]:
            cur_len = 1
        else:
            cur_len = 0
print(max_len)