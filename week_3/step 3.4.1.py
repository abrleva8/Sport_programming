# В верхнем-левом углу таблицы сидит черепаха. Она умеет ходить только вниз, вправо и вниз-вправо.
# В каждой клетке записано число, и черепашка прибавляет его к своей сумме, когда оказывается на клетке.
# Черепаха хочет попасть в нижнюю-правую клетку, получив в итоге минимально возможную сумму.
# Помогите ей - посчитайте, какую сумму она в итоге наберет?


# work if max_number < 1001
from sys import stdin

input = stdin.readline


def find_answer(arr):
    rows = len(arr)
    columns = len(arr[0])
    dp_arr = [[10 ** 9 + 1] * (columns + 1) for i in range(rows + 1)]

    dp_arr[0][0] = 0

    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            dp_arr[i][j] = min(dp_arr[i - 1][j - 1], dp_arr[i - 1][j], dp_arr[i][j - 1]) + arr[i - 1][j - 1]

    path = []
    x, y = rows, columns
    size_of_path = 0
    while x > 0 and y > 0:
        path.append([x, y])
        size_of_path += 1
        if dp_arr[x - 1][y] + arr[x - 1][y - 1] == dp_arr[x][y]:
            x -= 1
        elif dp_arr[x][y - 1] + arr[x - 1][y - 1] == dp_arr[x][y]:
            y -= 1
        else:
            x -= 1
            y -= 1
    path.append([dp_arr[rows][columns], size_of_path])
    return path


n, m = map(int, input().split())
arr = [[int(j) for j in input().split()] for i in range(n)]
result = find_answer(arr)
for i in reversed(range(len(result))):
    print(result[i][0], result[i][1])
