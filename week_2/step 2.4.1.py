# Вам даны два целых числа N и M (1 ≤ N ≤ 10^9, 2 ≤ M ≤ 10^9).
# Вычислите остаток от деления N^N на M.

def remain_nn_m(n, m, degree):
    if degree == 1:
        return n % m

    if degree % 2 == 0:
        tmp = remain_nn_m(n, m, degree//2) % m
        return (tmp * tmp) % m
    else:
        return (remain_nn_m(n, m, degree - 1) * (n % m)) % m

n, m = map(int, input().split())

result = remain_nn_m(n, m, n)
print(result)
