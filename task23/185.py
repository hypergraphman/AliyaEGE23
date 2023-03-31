def f(s, k):
    if k == 11:
        a.add(s)
        return None
    if k > 11:
        return None
    f(s - 2, k + 1)
    f(s * (-3), k + 1)


a = set()
f(91, 0)
new_a = []
for el in a:
    if el < 0:
        new_a.append(el)
print(len(new_a))
