# В этой задаче вам требуется проверить, что данный набор ребер может образовывать дерево обхода в глубину.

# need to rewrite in C++

from sys import stdin


def get_adjacency_list(list_of_edges, n):
    adjacency_list = [[] for _ in range(n + 1)]

    for edge in list_of_edges:
        adjacency_list[edge[0]].append(edge[1])
        adjacency_list[edge[1]].append(edge[0])

    return adjacency_list


def dfs(v: int):
    global answer
    used_of_tree[v] = True
    for u in adjacency_list_of_tree[v]:
        if used_of_tree[u]:
            continue
        dfs(u)

    for index, value in enumerate(used_of_tree):
        if used_of_tree[index]:
            continue
        for t in adjacency_list[index]:
            if t == v:
                answer += 1


answer = 0
n, m = map(int, input().split())
list_of_edges = [[int(i) for i in next(stdin).split()] for _ in range(m)]
q = int(next(stdin))

adjacency_list = get_adjacency_list(list_of_edges, n)

edges_of_tree = [list_of_edges[int(i) - 1] for i in next(stdin).split()]

adjacency_list_of_tree = get_adjacency_list(edges_of_tree, n)

if n != q + 1:
    answer += 1
else:
    for i in range(1, n + 1):
        used_of_tree = [False for _ in range(n + 1)]
        answer = 0
        dfs(i)
        if answer == 0:
            break

print('YES' if answer == 0 else 'NO')
