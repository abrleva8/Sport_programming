# Позиция максимума.
#
# Дан массив, требуется найти позицию максимального элемента. Если таких позиций несколько, найдите самую первую.
n = int(input())
lst = list(map(int, input().split()))

# a - array with int positive numbers
# @res - index of maximum number of @a
def position_of_maximum(a):
    maximum = 0

    for i in range(n):
        if a[i] > maximum:
            maximum = a[i]
            result = i + 1
    return result

res = position_of_maximum(lst)
print(res)
