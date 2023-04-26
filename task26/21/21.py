n, k, *a = map(int, open('26-k1.txt').read().split())

a.sort(reverse=True)
print(a[k], 0.2 * sum(a[:k]))
# 22
a = a[k:-k]
print(max(a), sum(a) / len(a))