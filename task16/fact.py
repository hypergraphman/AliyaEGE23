from functools import cache


@cache
def f(n):
    if n < 2:
        return 1
    else:
        return n * f(n - 1)


for i in range(100, 2000, 100):
    f(i)
print(f(2000))

p = 1
for i in range(1, 2001):
    p *= i
print(p)

a = [1, 1] + [0] * 4000
for i in range(2, 2001):
    a[i] = i * a[-1]
print(a[2000])
