# Префиксные суммы
#
# В этой задаче вам нужно будет много раз отвечать на запрос <<Найдите сумму чисел на отрезке в массиве>>.

n, q = map(int, input().split())
lst = list(map(int, input().split()))
part_sum = [0] * (n+1)

def partition_sum():
    part_sum[0] = 0
    for i in range(1, n+1):
        part_sum[i] = part_sum[i - 1] + lst[i - 1]

partition_sum()

for i in range(q):
    l, r = map(int, input().split())
    print(part_sum[r] - part_sum[l - 1])
