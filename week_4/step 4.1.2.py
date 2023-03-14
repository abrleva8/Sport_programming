# Дан граф, заданный своим списком ребер. Выведите его представление в виде списка смежности.

n, m = map(int, input().split())
list_of_edges = [[int(j) for j in input().split()] for i in range(m)]

adjacency_list = [[] for _ in range(n)]

for i in range(m):
    adjacency_list[list_of_edges[i][0] - 1].append(list_of_edges[i][1])
    adjacency_list[list_of_edges[i][1] - 1].append(list_of_edges[i][0])

for i in range(n):
    print(len(adjacency_list[i]), *sorted(adjacency_list[i]))
