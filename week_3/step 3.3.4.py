# В верхнем-левом углу таблицы сидит черепаха. Она умеет ходить только вниз, вправо и вниз-вправо.
# Каждая клетка доски либо свободна, либо занята. Черепаха хочет попасть в нижнюю-правую клетку.
# Сколькими способами она может это сделать?


def _find_answer(arr, prime):
    rows = len(arr)
    columns = len(arr[0])
    dp_arr = [[0] * (columns + 1) for i in range(rows + 1)]
    dp_arr[0][0] = 1
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            dp_arr[i][j] = (dp_arr[i - 1][j - 1] + dp_arr[i][j - 1] + dp_arr[i - 1][j]) % prime \
                if arr[i - 1][j - 1] == 0 else 0

    return dp_arr[rows][columns]


n, m = map(int, input().split())
arr = [[int(j) for j in input().split()] for i in range(n)]
prime = 10 ** 9 + 9
result = _find_answer(arr, prime)
print(result)
