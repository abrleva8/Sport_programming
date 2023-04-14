# В этой задаче требуется найти топологическую сортировку ориентированного графа, если она существует.

def get_adjacency_list(list_of_edges, n):
    adjacency_list = [[] for _ in range(n + 1)]

    for edge in list_of_edges:
        adjacency_list[edge[0]].append(edge[1])

    return adjacency_list


def dfs(v: int, k):
    global has_cycle, answers, pos
    used[v] = GRAY
    for u in adjacency_list[v]:
        if used[u] == GRAY:
            has_cycle = True
        if used[u] == WHITE:
            dfs(u, k)
    used[v] = BLACK
    answers[pos] = v
    pos = pos - 1


WHITE, GRAY, BLACK = -1, 0, 1

n, m = map(int, input().split())

answers = [-1] * (n + 1)
pos = n
list_of_edges = [[int(j) for j in input().split()] for _ in range(m)]
k = 0
used = [WHITE] * (n + 1)
has_cycle = False

adjacency_list = get_adjacency_list(list_of_edges, n)

for i in range(1, n + 1):
    if used[i] == WHITE:
        k += 1
        dfs(i, k)
    if has_cycle:
        break

print("NO" if has_cycle else "YES")
if not has_cycle:
    print(*answers[1::])
