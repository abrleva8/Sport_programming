# У вас есть n слитков золота, каждый имеет свой вес и стоимость. Также у вас есть рюкзак вместимости S.
# Необходимо вычислить максимальную суммарную стоимость камней, которую вы можете получить. Вы не можете дробить слитки.

from sys import stdin


def knapsack(s, ws, vs):
    global idx
    dp = [0] * (s + 1)
    paths = [[None] * (s + 1)] * (len(ws) + 1)
    free, free_v = [], 0
    for idx in range(len(ws)):
        paths[idx] = paths[idx - 1][:]
        if not vs[idx] or ws[idx] > s:
            continue
        if not ws[idx]:
            free.append(idx + 1)
            free_v += vs[idx]
            continue
        for w in range(s, ws[idx] - 1, -1):
            new = vs[idx] + dp[w - ws[idx]]
            if new > dp[w]:
                dp[w] = new
                paths[idx][w] = idx
    path, idx = free, paths[idx][s]
    while idx is not None:
        path.append(idx + 1)
        s -= ws[idx]
        idx = paths[idx - 1][s]
    return free_v + dp[-1], path


reader = (map(int, line.split()) for line in stdin)
s, n = next(reader)
ws, vs = map(list, reader)
v, path = knapsack(s, ws, vs)
print(v, len(path))
print(*path)
