# Многочлен
# Дан многочлен нечетной степени, требуется найти его корень.

def f(coefficients, x):
    result = 0
    temp = 1
    degree = len(coefficients)
    for i in reversed(range(degree)):
        result += coefficients[i] * temp
        temp *= x
    return result


def root_of_function(coefficients):
    eps = 1e-07
    left = -50
    right = 50
    while abs(f(coefficients, (left + right) / 2)) > eps:
        mid = (right + left) / 2
        if f(coefficients, mid) > 0:
            right = mid
        else:
            left = mid
    return (right + left) / 2


n = int(input())
a = [int(i) for i in input().split()]

res = root_of_function(a)
print(res)