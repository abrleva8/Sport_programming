# Дан граф, заданный своей матрицей смежности. Выведите его представление в виде списка ребер.

n = int(input())
adjacency_matrix = [list(map(int, input())) for i in range(n)]

list_of_edges = [(i + 1, j + 1) for i in range(n) for j in range(i, n) if adjacency_matrix[i][j] == 1]

print(len(list_of_edges))
for elem in list_of_edges:
    print(*elem)
