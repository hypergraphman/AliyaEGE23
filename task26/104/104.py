from collections import defaultdict

f = open('26-104.txt')
n, k = map(int, f.readline().split())
d = defaultdict(set)
for _ in range(n):
    row, pix = map(int, f.readline().split())
    d[row].add(pix)

mx_line = 0
mx_row = 0
for row in sorted(d.keys()):
    pixs = sorted(d[row])
    ln = 1
    n_line = 0
    for p1, p2 in zip(pixs, pixs[1:]):
        if p1 + 1 == p2:
            ln += 1
        else:
            if ln >= k:
                n_line += 1
            ln = 1
    if ln >= k:
        n_line += 1
    if n_line >= mx_line:
        mx_line = n_line
        mx_row = row
print(mx_line, mx_row)