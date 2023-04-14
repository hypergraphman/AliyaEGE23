a = [int(x) for x in open('17-1.txt').readlines()]
avg = sum(a) / len(a)
res = []

for i in range(len(a) - 2):
    if (a[i] < avg) + (a[i + 1] < avg) + (a[i + 2] < avg) >= 1:
       if (abs(a[i]) % 10 == 6) + (abs(a[i + 1]) % 10 == 6) + (abs(a[i + 2]) % 10 == 6) >= 1:
          res.append(a[i] + a[i + 1] + a[i + 2])
print(len(res))