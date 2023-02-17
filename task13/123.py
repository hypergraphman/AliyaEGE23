g = {
    'a': 'v',
    'b': 'ad',
    'v': 'e',
    'g': 'bvd',
    'd': 'z',
    'e': 'y',
    'y': 'gk',
    'z': 'y',
    'k': 'z',
}
paths = set()


def find_path(s, e, p):
    if len(p) > 1 and p[-1] != 'y' and len(set(p)) < len(p):
        return None
    if len(p) > 1 and s == e:
        paths.add(p)
        return None
    for v in g[s]:
        find_path(v, e, p + v)


find_path('y', 'y', 'y')
print(paths)
print(len(paths))