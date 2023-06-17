f = open('26_7602.txt')
k = int(f.readline())
n = int(f.readline())
a = []
for _ in range(n):
    p1, p2 = map(int, f.readline().split())
    a.append((p1, p2))
a.sort()
boxes = [0] * (k + 1)
c = 0
last = 0
for el in a:
    p1, p2 = el
    for i in range(1, k + 1):
        if boxes[i] < p1:
            boxes[i] = p2
            c += 1
            last = i
            break
print(c, last)