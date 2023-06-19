s = open('24gen.txt').read()
# если ищем минальную длину подстроки содержащую 210 символов Т
i_t = []
for i in range(len(s)):
    if s[i] == 'T':
        i_t.append(i)
min_L = 10**20
for i in range(210, len(i_t)):
    min_L = min(min_L, i_t[i] - i_t[i - 209])
print(min_L+1)

# если ищем максимальную длину подстроки содержащую 210 символов Т
i_t = []
for i in range(len(s)):
    if s[i] == 'T':
        i_t.append(i)
mx = 0 # изменение тут
for i in range(212, len(i_t)): # изменение тут
    mx = max(mx, i_t[i] - i_t[i - 211]) # Тут
print(mx - 1) # и тут