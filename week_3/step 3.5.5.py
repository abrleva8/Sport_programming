# У вас есть n слитков золота, каждый имеет свой вес и стоимость. Также у вас есть рюкзак вместимости S.
# Необходимо вычислить максимальную суммарную стоимость слитков,
# которую вы можете получить. Вы не можете дробить слитки.

# TLE - need to rewrite in C++

def find_answer(weights, w):
    inf = 3 * 10**6 + 1
    n = len(weights)
    dp = [[-inf] * (w + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(1, n + 1):
        for j in range(w + 1):
            if j >= weights[i - 1][0]:
                dp[i][j] = max(dp[i - 1][j - weights[i - 1][0]] + weights[i - 1][1], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp


s, n = map(int, input().split())
weights = [[int(i)] for i in input().split()]
costs = [int(i) for i in input().split()]

for i in range(n):
    weights[i].append(costs[i])
_dp = find_answer(weights, s)
print(max(_dp[n]))
