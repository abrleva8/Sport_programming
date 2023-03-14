# Дан граф, заданный своей матрицей смежности. Выведите его представление в виде списка смежности.

n = int(input())
adjacency_matrix = [list(map(int, input())) for i in range(n)]

adjacency_list = [[j + 1 for j in range(n) if adjacency_matrix[i][j] == 1] for i in range(n)]

for i in range(n):
    print(len(adjacency_list[i]), *adjacency_list[i])
