# На входе задан многочлен f(x)f(x) вида a_n*x^n+a_{n-1} * x^{n-1}+...+a_1 * x+a_0
# В первой строке задано одно целое число - степень многочлена n  (1≤n≤1000),
# а также некоторое целое число M (2≤M≤2025),во второй задаются n+1 целых чисел -
# коэффициенты многочлена, начиная с a_n и заканчивая a_0 (-10^6 <= a_i <= 10^6−10).
# Найдите такое минимальное целое неотрицательное x, что f(x) делится на M, или выведите -1 в случае, если таких x нет.


def f(a, x, m):
    result = 0
    tmp_x = 1
    for el in reversed(a):
        result = (result + (el % m) * tmp_x) % m
        tmp_x = (tmp_x * x) % m
    return result


n, m = map(int, input().split())
a = [int(i) for i in input().split()]
x = 1

while f(a, x, m) != 0:
    x += 1
    if x == m + 1:
        break
if x == m + 1:
    print(-1)
else:
    print(x)
