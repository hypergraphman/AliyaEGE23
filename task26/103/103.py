f = open('26-103.txt')
n, k, m = map(int, f.readline().split())
a = []
for _ in range(n):
    size, color = f.readline().split()
    size = int(size)
    a.append((size, color))
a.sort()
blocks = []
n_m = 0
while a:
    block = []
    if not block:
        block.append(a.pop())
    i = len(a) - 1
    while i >= 0 and len(block) < m:
        if block[-1][0] - a[i][0] >= k and block[-1][1] != a[i][1]:
            block.append(a.pop(i))
        i -= 1
    if len(block) == m:
        n_m += 1
    blocks.append(block)
print(len(blocks), n_m)