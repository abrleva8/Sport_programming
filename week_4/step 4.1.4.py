# Дан граф, заданный своим списком смежности. Выведите его представление в виде матрицы смежности.

n = int(input())

adjacency_list = [list(map(int, input().split())) for i in range(n)]

adjacency_matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(1, len(adjacency_list[i])):
        adjacency_matrix[i][adjacency_list[i][j] - 1] = 1

for i in range(n):
    print(''.join(map(str, adjacency_matrix[i])))
