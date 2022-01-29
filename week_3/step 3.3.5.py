# В верхней левой клетке доски сидит конь. Он умеет ходить, как показано на рисунке.
# Необходимо посчитать количество способов, которым этот конь может добраться до нижней правой клетки доски.

def _find_answer(n, m, prime=10**9 + 123):
    dp = [[0] * (m + 3) for _ in range(n + 3)]
    dp[1][0] = 1
    k = 2
    i, j = 2, k
    while i + j <= m + n + 2:
        while i >= 2 and j >= 2:
            if i <= n + 1 and 2 <= j <= m + 1:
                dp[i][j] = (dp[i + 1][j - 2] + dp[i - 1][j - 2] + dp[i - 2][j - 1] + dp[i - 2][j + 1]) % prime
            i += 1
            j -= 1
        k += 1
        i, j = 2, k

    return dp[n + 1][m + 1]


n, m = map(int, input().split())
print(_find_answer(n, m))
