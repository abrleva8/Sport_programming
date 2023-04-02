# Дан связный неориентированный граф, заданный своим списком ребер. Требуется выделить дерево обхода графа в глубину.

def dfs(v: int):
    used[v] = True
    for u in adjacency_list[v]:
        if used[u]:
            continue
        path.append(v)
        dfs(u)
    path.append(v)


def get_number_of_edge(a, b):
    for i in range(len(list_of_edges)):
        if a == list_of_edges[i][0] and b == list_of_edges[i][1]:
            return i + 1


def get_traversal_tree(path):
    for i in range(len(path) - 1):
        if path[i] < path[i + 1]:
            tree.append(get_number_of_edge(path[i], path[i + 1]))


n, m = map(int, input().split())

list_of_edges = [[int(j) for j in input().split()] for _ in range(m)]

path, tree = [], []
used, adjacency_list = [False for _ in range(n + 1)], [[] for _ in range(n + 1)]

for edge in list_of_edges:
    adjacency_list[edge[0]].append(edge[1])
    adjacency_list[edge[1]].append(edge[0])

dfs(1)
get_traversal_tree(path)
print(n - 1)
print(*tree)
