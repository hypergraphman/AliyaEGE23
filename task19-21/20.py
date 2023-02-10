a = [[0 for i in range(100)]for j in range(100)]

for i in range(100):
    for j in range(100):
        if i*2+j >= 77 or i+j*2 >= 77:
            a[i][j] = 1
        else:
            a[i][j] = 0
for i in range(100):
    print(a[i])
for _ in range(10):
    for i in range(100):
        for j in range(100):
            if a[i][j] == 0:
                if (a[i+1][j] > 0 and a[i][j+1] > 0 and
                   a[i*2][j] > 0 and a[i][j*2] > 0):
                    a[i][j] = max(a[i+1][j], a[i][j+1],
                                  a[i*2][j], a[i][j*2])*(-1)
                elif (a[i+1][j] < 0 or a[i][j+1] < 0 or
                     a[i*2][j] < 0 or a[i][j*2] < 0):
                    a[i][j] = min(a[i+1][j], a[i][j+1],
                                  a[i*2][j], a[i][j*2])*(-1)+1
for i in range(70):
    if a[7][i] == 2: #сюда пишем 2 для №20 и -2 для №21
        print(i) 
