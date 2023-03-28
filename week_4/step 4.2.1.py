def dfs(v: int):
    used[v] = True
    for u in adjacency_list[v]:
        if used[u]:
            continue
        path.append(v + 1)
        dfs(u)
    path.append(v + 1)


n, m = map(int, input().split())

list_of_edges = [[int(j) - 1 for j in input().split()] for i in range(m)]

start_vertex = int(input())
path = []

adjacency_list = [[] for _ in range(n)]
used = [False] * n

for i in range(m):
    adjacency_list[list_of_edges[i][0]].append(list_of_edges[i][1])
    adjacency_list[list_of_edges[i][1]].append(list_of_edges[i][0])

dfs(start_vertex - 1)
print(len(path))
print(*path)
