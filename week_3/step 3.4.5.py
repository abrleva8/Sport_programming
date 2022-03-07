# В верхней левой клетке доски сидит ладья. Она умеет ходить на любое количество клеток вправо и на любое количество
# клеток вниз. В каждой клетке доски написано число. Необходимо добраться до нижней правой клетки, набрав минимально
# возможную сумму.


def find_answer(n, m, arr):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    part_sum_columns = [[0] * (m + 1) for _ in range(n + 1)]
    part_sum_rows = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = arr[0][0]
    part_sum_columns[1][1] = arr[0][0]
    part_sum_rows[1][1] = arr[0][0]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == j == 1:
                continue
            if i == 1:
                dp[i][j] = part_sum_rows[i][j - 1] + arr[i - 1][j - 1]
                part_sum_columns[i][j] = dp[i][j]
                part_sum_rows[i][j] = min(part_sum_rows[i][j - 1], dp[i][j])
            elif j == 1:
                dp[i][j] = part_sum_columns[i - 1][j] + arr[i - 1][j - 1]
                part_sum_rows[i][j] = dp[i][j]
                part_sum_columns[i][j] = min(part_sum_columns[i - 1][j],  dp[i][j])
            else:
                dp[i][j] = min(part_sum_columns[i - 1][j], part_sum_rows[i][j - 1]) + arr[i - 1][j - 1]
                part_sum_columns[i][j] = min(part_sum_columns[i - 1][j],  dp[i][j])
                part_sum_rows[i][j] = min(part_sum_rows[i][j - 1], dp[i][j])

    return dp


def get_path(dp):
    x, y = len(dp) - 1, len(dp[0]) - 1
    path = []
    while x > 0 and y > 0:
        path.append([x, y])
        min_el = 1_000_000_001
        min_index_i, min_index_j = 0, 0
        for i in range(1, x):
            if dp[i][y] < min_el:
                min_el = dp[i][y]
                min_index_i, min_index_j = i, y
        for j in range(1, y):
            if dp[x][j] < min_el:
                min_el = dp[x][j]
                min_index_i, min_index_j = x, j
        x, y = min_index_i, min_index_j
    return path


n, m = map(int, input().split())
arr = [[int(j) for j in input().split()] for i in range(n)]
_dp = find_answer(n, m, arr)
_path = get_path(_dp)
print(_dp[n][m], len(_path))
for i in reversed(range(len(_path))):
    print(*_path[i])
