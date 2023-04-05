# В данной задаче вам нужно проверить, есть ли цикл в неориентированном графе.

def get_adjacency_list(list_of_edges, n):
    adjacency_list = [[] for _ in range(n + 1)]

    for edge in list_of_edges:
        adjacency_list[edge[0]].append(edge[1])
        adjacency_list[edge[1]].append(edge[0])

    return adjacency_list


def dfs(v: int, k):
    used[v] = k
    component.append(v)
    for u in adjacency_list[v]:
        if used[u]:
            continue
        dfs(u, k)


n, m = map(int, input().split())

list_of_edges = [[int(j) for j in input().split()] for _ in range(m)]

used, k = [0] * (n + 1), 0
has_cycle = False
adjacency_list = get_adjacency_list(list_of_edges, n)

for i in range(1, n + 1):
    component, total_edges = [], 0
    if used[i] != 0:
        continue
    k += 1
    dfs(i, k)
    for t in component:
        total_edges += len(adjacency_list[t])
    if total_edges / 2 != len(component) - 1:
        has_cycle = True
        break

print("YES" if has_cycle else "NO")
