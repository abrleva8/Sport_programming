# В верхнем-левом углу таблицы сидит черепаха. Она умеет ходить только вниз, вправо и вниз-вправо.
# В каждой клетке записано число, и черепашка прибавляет его к своей сумме, когда оказывается на клетке.
# Черепаха хочет попасть в нижнюю-правую клетку, получив в итоге минимально возможную сумму.
# Помогите ей - посчитайте, какую сумму она в итоге наберет?
# TLE

def find_answer(arr):
    rows = len(arr)
    columns = len(arr[0])
    dp_arr = [[0] * columns for i in range(rows)]

    dp_arr[0][0] = arr[0][0]
    for j in range(1, columns):
        dp_arr[0][j] = dp_arr[0][j - 1] + arr[0][j]

    for i in range(1, rows):
        dp_arr[i][0] = dp_arr[i - 1][0] + arr[i][0]

    for i in range(1, rows):
        for j in range(1, columns):
            dp_arr[i][j] = min(dp_arr[i - 1][j - 1], dp_arr[i][j - 1], dp_arr[i - 1][j]) + arr[i][j]

    return dp_arr[rows - 1][columns - 1]

n, m = map(int, input().split())
arr = [[int(j) for j in input().split()] for i in range(n)]
result = find_answer(arr)
print(result)
