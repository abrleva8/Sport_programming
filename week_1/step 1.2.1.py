# Сумма чисел в массиве.
#
# В этой задаче все предельно просто - дан массив, требуется посчитать сумму чисел в нем.
n = int(input())
lst = list(map(int, input().split()))

# a - array with int numbers
# @res - sum of @a
def sum_of_array(a):
    result = 0
    for x in a:
        result += x
    return result

res = sum_of_array(lst)
print(res)
