# Дан неориентированный граф, заданный своим списком ребер. Требуется определить компоненты связности в нем.

import sys

sys.setrecursionlimit(10 ** 9)


def dfs(v: int, k: int):
    used[v] = k
    for u in adjacency_list[v]:
        if used[u]:
            continue
        dfs(u, k)


n, m = map(int, input().split())

adjacency_list = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    adjacency_list[a].append(b)
    adjacency_list[b].append(a)

used, k = [0] * (n + 1), 0

for i in range(1, n + 1):
    if used[i] == 0:
        k += 1
        dfs(i, k)

print(k)
print(*used[1:])
