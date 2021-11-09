# Найти наибольший общий делитель N целых положительных чисел.
#
# В первой строке входных данных находится одно целое положительное число N, не меньшее 2 и не превосходящее 100.
# Вторая строка содержит N целых положительных чисел, не превосходящих 10^6, НОД которых надо найти.
def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)


# @arr is array with inetger numbers,
# the method returns gcd all of numbers in @arr
def gcd_n(arr):
    result = arr[0]
    for el in arr:
        result = gcd(result, el)
        if result == 1:
            return 1
    return result


n = int(input())
arr = [int(i) for i in input().split()]
result = gcd_n(arr)
print(result)
