# В этой задаче требуется выяснить, сколько шагов сделает бинарный поиск

import sys

input_ = sys.stdin.readline


def count_of_request(n, k):
    l = -1
    r = n
    count = 0
    while l + 1 < r:
        mid = (l + r) // 2
        if mid < k:
            l = mid
        else:
            r = mid
        count += 1
    return count


n, m = map(int, input_().split())
for i in range(m):
    k = int(input_())
    print(count_of_request(n, k))
