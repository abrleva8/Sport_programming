# Дан связный неориентированный граф. Требуется найти сумму расстояний между всеми неупорядоченными парами вершин.


import sys
from collections import deque

input = sys.stdin.readline


def get_adjacency_list(_list_of_edges, _n):
    _adjacency_list = [[] for _ in range(_n + 1)]

    for edge in _list_of_edges:
        _adjacency_list[edge[0]].append(edge[1])
        _adjacency_list[edge[1]].append(edge[0])

    return _adjacency_list


def bfs(_s):
    global adjacency_list
    dists = [-1] * (n + 1)
    q = deque()
    q.append(_s)
    dists[_s] = 0
    while q:
        _v = q[0]
        q.popleft()
        for u in adjacency_list[_v]:
            if dists[u] == -1:
                q.append(u)
                dists[u] = dists[_v] + 1
    return sum(dists[1::])


n, m = map(int, input().split())
list_of_edges = [[int(j) for j in input().split()] for _ in range(m)]

adjacency_list = get_adjacency_list(list_of_edges, n)
total = sum([bfs(i) for i in range(1, n + 1)]) // 2
print(total)
