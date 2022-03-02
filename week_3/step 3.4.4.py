# В верхней левой клетке доски сидит конь. Он умеет ходить, как показано на рисунке. В каждой клетке доски написано
# число. Необходимо добраться до нижней правой клетки, набрав минимально возможную сумму.

import sys


def f(i, j):
    global dp, arr, parent_x, parent_y
    if i < 2 or j < 2 or i >= n + 2 or j >= m + 2:
        return 10 ** 14
    elif i == 2 and j == 2:
        return arr[0][0]
    elif dp[i][j] != 10 ** 14:
        return dp[i][j]

    dp[i][j] = min(f(i - 2, j + 1), f(i - 2, j - 1), f(i - 1, j - 2), f(i + 1, j - 2)) + arr[i - 2][j - 2]
    if dp[i][j] == dp[i - 2][j + 1] + arr[i - 2][j - 2]:
        parent_x[i][j] = i - 2
        parent_y[i][j] = j + 1
    elif dp[i][j] == dp[i - 2][j - 1] + arr[i - 2][j - 2]:
        parent_x[i][j] = i - 2
        parent_y[i][j] = j - 1
    elif dp[i][j] == dp[i - 1][j - 2] + arr[i - 2][j - 2]:
        parent_x[i][j] = i - 1
        parent_y[i][j] = j - 2
    else:
        parent_x[i][j] = i + 1
        parent_y[i][j] = j - 2

    return dp[i][j]


sys.setrecursionlimit(1500)
n, m = map(int, input().split())
arr = [[int(j) for j in input().split()] for i in range(n)]
dp = [[10 ** 14] * (m + 3) for _ in range(n + 3)]
dp[2][2] = arr[0][0]
parent_x = [[-1] * (m + 3) for _ in range(n + 3)]
parent_y = [[-1] * (m + 3) for _ in range(n + 3)]
res = f(n + 1, m + 1)
if res < 10 ** 13:
    print('YES')
    print(res, end=' ')
    answer = []
    x, y = n + 1, m + 1
    while x > 1 and y > 1:
        answer.append([x - 1, y - 1])
        old_x, old_y = x, y
        x = parent_x[old_x][old_y]
        y = parent_y[old_x][old_y]
    print(len(answer))
    for i in reversed(range(len(answer))):
        print(answer[i][0], answer[i][1])
else:
    print('NO')
