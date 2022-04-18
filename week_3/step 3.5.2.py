# У вас есть n слитков золота, каждый имеет свой вес. Также у вас есть рюкзак вместимости S. Необходимо вычислить
# максимальный вес, который вы можете с собой унести. Вы не можете дробить слитки.


def find_answer(arr, s):
    n = len(arr) - 1
    dp = [[0] * (s + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(s + 1):
            if dp[i - 1][j] == 1:
                dp[i][j] = 1
            elif arr[i] <= j:
                if dp[i - 1][j - arr[i]] == 1:
                    dp[i][j] = 1
    res = 0
    for w in range(s, -1, -1):
        if dp[n][w] == 1:
            res = w
            break
    return res


s, n = map(int, input().split())
arr = [0] + [int(i) for i in input().split()]
print(find_answer(arr, s))
