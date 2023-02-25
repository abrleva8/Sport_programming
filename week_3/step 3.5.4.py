# У вас есть n слитков золота, каждый имеет свой вес и стоимость. Также у вас есть рюкзак вместимости S.
# Необходимо вычислить максимальную суммарную стоимость слитков, которую вы можете получить. Вы можете дробить слитки.
# В таком случае стоимость слитка будет уменьшаться пропорционально весу слитка.

import math

s, n = map(int, input().split())
weights = [[int(i)] for i in input().split()]
costs = [int(i) for i in input().split()]

for i in range(n):
    weights[i].append(costs[i])

weights.sort(key=lambda x: x[0]/x[1] if x[1] != 0 else 10**6)

result, weight, i = 0, 0, 0

while i < n:
    if weight + weights[i][0] <= s:
        weight += weights[i][0]
        result += weights[i][1]
    else:
        result += (s - weight) / weights[i][0] * weights[i][1]
        break
    i += 1

print(math.ceil(result))
