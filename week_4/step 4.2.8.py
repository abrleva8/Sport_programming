# Дан неориентированный граф, требуется найти любой цикл в нем, либо сказать, что их нет.

def get_adjacency_list(list_of_edges, n):
    adjacency_list = [[] for _ in range(n + 1)]

    for edge in list_of_edges:
        adjacency_list[edge[0]].append(edge[1])
        adjacency_list[edge[1]].append(edge[0])

    return adjacency_list


def dfs(v: int, k):
    global has_cycle, answer, parent
    used[v] = GRAY
    for u in adjacency_list[v]:
        if not has_cycle and used[u] == WHITE:
            parent[u] = v
            dfs(u, k)
        if not has_cycle and used[u] == GRAY:
            if parent[v] != u:
                parent[u] = v
                has_cycle = True
                answer = u
                return
    used[v] = BLACK


def get_some_cycle(_parent, _answer):
    total = [_answer]
    _next_parent = _parent[_answer]
    while _next_parent != _answer:
        total.append(_next_parent)
        _next_parent = _parent[_next_parent]
    return total


WHITE, GRAY, BLACK = -1, 0, 1

n, m = map(int, input().split())

list_of_edges = [[int(j) for j in input().split()] for _ in range(m)]
answer, k = 0, 0
used, parent = [WHITE] * (n + 1), [0] * (n + 1)
has_cycle = False

adjacency_list = get_adjacency_list(list_of_edges, n)

for i in range(1, n + 1):
    if used[i] == WHITE:
        k += 1
        dfs(i, k)
    if has_cycle:
        next_parent = parent[answer]
        break

print("YES" if has_cycle else "NO")
if has_cycle:
    cycle = get_some_cycle(parent, answer)
    print(len(cycle))
    print(*cycle[::-1])
