s = "АБ БД ВАБ ГАВ ДВЖЕ ЕЖИЛК ЖГВ ИЛД КЖ ЛК"
g = {c[0]:c[1:] for c in s.split()}


def f(v, p):
    if len(p) > 1 and p[0] == p[-1]:
        return 1
    if len(p) > len(set(p)):
        return 0
    return sum(f(w, p + w) for w in g[v])


print(f('Ж', 'Ж'))