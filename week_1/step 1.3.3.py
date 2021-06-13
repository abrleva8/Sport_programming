# Есть ли число?
# В этой задаче вам надо будет много раз проверять, что число есть в данном массиве.

import sys

input = sys.stdin.readline


# arr is sorted array
def is_has_a_number(arr, number):
    l = -1
    r = len(arr)
    while l + 1 < r:
        mid = (l + r) // 2
        if arr[mid] < number:
            l = mid
        else:
            r = mid
    return r < len(arr) and arr[r] == number


n, m = map(int, input().split())
arr = [int(i) for i in input().split()]
for _ in range(m):
    if is_has_a_number(arr, int(input())):
        print("YES")
    else:
        print("NO")
