# В верхней левой клетке доски сидит ферзь. Он умеет ходить на любое количество клеток вправо,
# на любое количество клеток вниз, а также на любое количество клеток по диагонали вниз-вправо.
# В каждой клетке доски написано число. Необходимо добраться до нижней правой клетки, набрав минимально возможную сумму.

def find_answer(n, m, arr):
    global parent_x, parent_y
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    part_sum_columns = [[0] * (m + 1) for _ in range(n + 1)]
    part_sum_rows = [[0] * (m + 1) for _ in range(n + 1)]
    part_sum_diagonals = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = arr[0][0]
    part_sum_columns[1][1] = arr[0][0]
    part_sum_rows[1][1] = arr[0][0]
    part_sum_diagonals[1][1] = arr[0][0]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == j == 1:
                continue
            if i == 1:
                dp[i][j] = part_sum_rows[i][j - 1] + arr[i - 1][j - 1]
                part_sum_columns[i][j] = dp[i][j]
                part_sum_diagonals[i][j] = dp[i][j]
                part_sum_rows[i][j] = min(part_sum_rows[i][j - 1], dp[i][j])
            elif j == 1:
                dp[i][j] = part_sum_columns[i - 1][j] + arr[i - 1][j - 1]
                part_sum_rows[i][j] = dp[i][j]
                part_sum_diagonals[i][j] = dp[i][j]
                part_sum_columns[i][j] = min(part_sum_columns[i - 1][j], dp[i][j])
            else:
                dp[i][j] = min(part_sum_columns[i - 1][j], part_sum_rows[i][j - 1], part_sum_diagonals[i - 1][j - 1])\
                           + arr[i - 1][j - 1]
                part_sum_columns[i][j] = min(part_sum_columns[i - 1][j],  dp[i][j])
                part_sum_rows[i][j] = min(part_sum_rows[i][j - 1], dp[i][j])
                part_sum_diagonals[i][j] = min(part_sum_diagonals[i - 1][j - 1], dp[i][j])

    return dp


def get_path(dp):
    global parent_x, parent_y
    x, y = len(dp) - 1, len(dp[0]) - 1
    path = []

    while x > 0 and y > 0:
        path.append([x, y])

        if x == y == 1:
            break

        tmp_x, tmp_xx = x - 1, x - 1
        while dp[tmp_x][y] + arr[x - 1][y - 1] != dp[x][y] and tmp_x > 0:
            tmp_x -= 1
        if tmp_x > 0:
            x = tmp_x
            continue

        tmp_y, tmp_yy = y - 1, y - 1
        while dp[x][tmp_y] + arr[x - 1][y - 1] != dp[x][y] and tmp_y > 0:
            tmp_y -= 1

        if tmp_y > 0:
            y = tmp_y
            continue

        tmp_xx, tmp_yy = x - 1, y - 1
        while dp[tmp_xx][tmp_yy] + arr[x - 1][y - 1] != dp[x][y] and tmp_xx > 0 and tmp_yy > 0:
            tmp_xx -= 1
            tmp_yy -= 1
        if tmp_xx > 0 and tmp_yy > 0:
            x, y = tmp_xx, tmp_yy
            continue

    return path


n, m = map(int, input().split())
arr = [[int(j) for j in input().split()] for i in range(n)]
parent_x = [[-1] * (m + 1) for _ in range(n + 1)]
parent_y = [[-1] * (m + 1) for _ in range(n + 1)]
_dp = find_answer(n, m, arr)
_path = get_path(_dp)
print(_dp[n][m], len(_path))
for i in reversed(range(len(_path))):
    print(*_path[i])
