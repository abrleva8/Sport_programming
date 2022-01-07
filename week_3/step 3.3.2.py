# Отряду нужно пересечь прямоугольное поле размера m×n квадратов, двигаясь из левого верхнего угла в правый нижний
# и перемещаясь между соседними квадратами только в двух направлениях - вправо и вниз.
# Поле не очень ровное, но у отряда есть карта, на которой отмечена высота каждого квадрата.
# Опасность перехода с квадрата высоты h_1 на соседний квадрат высоты h_2 оценивается числом |h_2 - h_1|
# опасность всех переходов в пути суммируется.
# Выясните, какова минимальная опасность пути из квадрата (1,1) в квадрат (m,n).

def find_answer(arr):
    rows = len(arr)
    columns = len(arr[0])
    dp_arr = [[0] * columns for i in range(rows)]

    for j in range(1, columns):
        dp_arr[0][j] = dp_arr[0][j - 1] + abs(arr[0][j] - arr[0][j - 1])

    for i in range(1, rows):
        dp_arr[i][0] = dp_arr[i - 1][0] + abs(arr[i][0] - arr[i - 1][0])

    for i in range(1, rows):
        for j in range(1, columns):
            dp_arr[i][j] = min(dp_arr[i][j - 1] + abs(arr[i][j - 1] - arr[i][j]),\
                               dp_arr[i - 1][j] + abs(arr[i - 1][j] - arr[i][j]))

    return dp_arr[rows - 1][columns - 1]


m, n = map(int, input().split())
arr = [[int(j) for j in input().split()] for i in range(n)]
result = find_answer(arr)
print(result)
