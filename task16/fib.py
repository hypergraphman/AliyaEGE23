from time import time
from functools import cache


@cache
def f(n):
    if n < 3:
        return 1
    else:
        return f(n - 1) + f(n - 2)


for i in range(400, 4000, 400):
    f(i)
print(f(2000))


prev = 1
cur = 1
for i in range(3, 2000 + 1):
    prev, cur = cur, prev + cur
print(cur)