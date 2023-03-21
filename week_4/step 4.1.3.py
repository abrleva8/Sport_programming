# Дан граф, заданный своим списком ребер. Выведите его представление в виде матрицы смежности.

n, m = map(int, input().split())
list_of_edges = [[int(j) for j in input().split()] for i in range(m)]

adjacency_matrix = [[0] * n for _ in range(n)]

for i in range(m):
    adjacency_matrix[list_of_edges[i][0] - 1][list_of_edges[i][1] - 1] = 1
    adjacency_matrix[list_of_edges[i][1] - 1][list_of_edges[i][0] - 1] = 1

for i in range(n):
    print(''.join(map(str, adjacency_matrix[i])))
