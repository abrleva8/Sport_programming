# Меньше либо равно

# В этой задаче вам нужно будет несколько раз находить в отсортированном массиве первое число,
# которое меньше либо равно числу из запроса. Обратите внимание - в этой задаче массив нумеруется с единицы.


import sys
input = sys.stdin.readline


def first_bigger_element(array, element):
    l = -1
    r = len(array)
    while l + 1 < r:
        mid = (l + r) // 2
        if array[mid] > element:
            l = mid
        else:
            r = mid
    if r == len(array):
        return "NO SOLUTION"
    else:
        return r + 1


n, m = map(int, input().split())
arr = [int(i) for i in input().split()]
for _ in range(m):
    print(first_bigger_element(arr, int(input())))
