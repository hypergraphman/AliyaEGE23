from string import ascii_uppercase

f = open('24-164.txt')
mx = 0
for line in f.readlines():
    if line.count('E') < 20:
        for char in ascii_uppercase:
            mx = max(mx, line.rfind(char) - line.find(char))
print(mx)