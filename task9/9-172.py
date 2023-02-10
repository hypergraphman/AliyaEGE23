# Автор: А. Рогов
reader = open('9-170.txt').readlines()
k = 0
for line in reader:
    line = [int(i) for i in line.split()]
    repeat = {i for i in line if line.count(i) == 2}
    single = {i for i in line if line.count(i) == 1}
    if len(repeat) > 0 and all(i > j for i in repeat for j in single):
        k += 1
print(k)
