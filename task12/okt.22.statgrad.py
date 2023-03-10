def alg(line):
    while '00' not in line:
        line = line.replace('011', '20', 1)
        line = line.replace('022', '10', 1)
        line = line.replace('01', '220', 1)
        line = line.replace('02', '110', 1)
    return line


i = '022122212221212121212121212121212121212111111111121212121210'
print(i.count('1'), i.count('2'))
t = alg(i)
print(t.count('1'), t.count('2'))