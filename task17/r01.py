k = 0
mx = 0
for i in range(1017, 7937 + 1, 3):
    if i % 7 and i % 17 and i % 19 and i % 27:
        k += 1
        mx = i
print(k, mx)
