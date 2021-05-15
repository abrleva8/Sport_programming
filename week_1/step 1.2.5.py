# Максимальная сумма
#
# В этой задаче вам требуется найти непустой отрезок массива с максимальной суммой.

n = int(input())
lst = list(map(int, input().split()))
part_sum = [0] * n

min_sum = 100000000000000000000;
max_sum = -100000000000000000000;

for i in range(n):
    part_sum[i] = part_sum[i - 1] + lst[i]

    max_sum = max(lst[i], part_sum[i] - min_sum, part_sum[i], max_sum)

    if part_sum[i] < min_sum:
        min_sum = part_sum[i]

print(max_sum)
