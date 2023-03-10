from collections import defaultdict

d = defaultdict(list)
n = int(input())
a = [int(x) for x in input().split()]
cur_len = 1
for i in range(1, len(a)):
    if a[i - 1] == a[i]:
        cur_len += 1
    else:
        d[a[i-1]].append(cur_len)
        cur_len = 1
d[a[-1]].append(cur_len)

mx = 0
for key in d.keys():
    mx = max(sum(sorted(d[key])[:2]), mx)
print(mx)