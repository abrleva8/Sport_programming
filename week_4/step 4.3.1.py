# Волновым обходом графа из вершины v называется такая последовательность вершин u1, u2 … un, что:
# u1 = v
# Каждая вершина встречается в последовательности ровно 1 раз и
# Все вершины можно разделить на <<волны>>. Каждая волна - несколько подряд идущих вершин.
# У каждой вершины (кроме первой) существует вершина из предыдущей волны, с которой она связана и
# Нет таких вершин из более ранних волн.
# Вам задан связный неориентированный граф, выведите любой его волновой обход.
from collections import deque
from typing import List


def get_adjacency_list(_list_of_edges, _n) -> List[object]:
    _adjacency_list = [[] for _ in range(_n + 1)]

    for edge in _list_of_edges:
        _adjacency_list[edge[0]].append(edge[1])
        _adjacency_list[edge[1]].append(edge[0])

    return _adjacency_list


def bfs(_s):
    q = deque()
    q.append(_s)
    used[_s] = True
    _path = [_s]
    while q:
        _v = q[0]
        q.popleft()
        for u in adjacency_list[_v]:
            if used[u]:
                continue
            q.append(u)
            used[u] = True
            _path.append(u)
    return _path


n, m = map(int, input().split())
list_of_edges = [[int(j) for j in input().split()] for _ in range(m)]
v = int(input())

used = [False] * (n + 1)

adjacency_list = get_adjacency_list(list_of_edges, n)
path = bfs(v)
print(*path)
