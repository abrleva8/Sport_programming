# В этой задаче дан ориентированный граф и некоторый порядок вершин.
# Требуется проверить, что вершины, следующие в данном порядке образуют топологическую сортировку.

import sys

input = sys.stdin.readline


def get_adjacency_list(_list_of_edges, _n):
    _adjacency_list = [[] for _ in range(_n + 1)]

    for edge in _list_of_edges:
        _adjacency_list[edge[0]].append(edge[1])

    return _adjacency_list


n, m = map(int, input().split())
list_of_edges = [[int(j) for j in input().split()] for _ in range(m)]
checking_order = [int(j) for j in input().split()]
value = range(n)
dict_check_order = dict(zip(checking_order, value))
is_topology_sort_order = True

for pair in list_of_edges:
    if dict_check_order[pair[0]] >= dict_check_order[pair[1]]:
        is_topology_sort_order = False
        break
print("YES" if is_topology_sort_order else "NO")
