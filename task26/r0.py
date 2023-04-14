# f = open('26.txt')
# v, n = map(int, f.readline().split())
# a = list(map(int, f.readlines()))
for i in range(1, 21):
    v, n, *a = map(int, open(f'26-{i}.txt').read().split())
    a.sort()
    k = 0
    while k < n and v >= a[k]:
        v -= a[k]
        k += 1
    print(i, k, end=' ')
    v += a[k - 1]
    while k < n and v >= a[k]:
        k += 1
    print(a[k - 1])
