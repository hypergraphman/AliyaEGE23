from itertools import permutations


def alg(n):
    nums = []
    for x in permutations(str(n), r=2):
        num = int(''.join(x))
        if 10 <= num <= 99:
            nums.append(num)
    return max(nums) - min(nums)


i = 100
while alg(i) != 40:
    i += 1
print(i)

# теперь ищем наибольшее == 40
mx = 0
for i in range(100, 1000):
    if alg(i) == 40 and i > mx:
        mx = i
print(mx)
