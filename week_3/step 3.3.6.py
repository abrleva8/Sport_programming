# В верхней левой клетке доски сидит ладья. Она умеет ходить на любое количество клеток вправо и вниз.
# Необходимо посчитать количество способов, которым эта ладья может добраться до нижней правой клетки доски.

def find_answer(n, m, prime=10**9 + 33):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    part_sum_columns = [[0] * (m + 1) for _ in range(n + 1)]
    part_sum_rows = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1], part_sum_columns[1][1],  part_sum_rows[1][1] = 1, 1, 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == j == 1:
                continue
            dp[i][j] = (part_sum_columns[i - 1][j] + part_sum_rows[i][j - 1]) % prime
            part_sum_columns[i][j] = (part_sum_columns[i - 1][j] + dp[i][j]) % prime
            part_sum_rows[i][j] = (part_sum_rows[i][j - 1] + dp[i][j]) % prime
    return dp[n][m]


n, m = map(int, input().split())
result = find_answer(n, m)
print(result)
