n = int(input())
a = list(map(int, input().split()))
k = 1
print(a[0], end=' ')
for i in range(1, len(a)):
    x, y = a[i - 1], a[i]
    if x == y:
        k += 1
        if k < 3:
            print(y, end=' ')
    else:
        k = 1
        print(y, end=' ')