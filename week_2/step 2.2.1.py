# Последовательность Фибоначчи задаётся следующим образом. F(0)=F(1)=1, для всех N>1 F(N)=F(N-1)+F(N-2).
# Вам задано целое число N, 1 <= N <= 10^4
# Вычислите остаток от деления F(N) на  10^6+31

# @n is a whole number
# @r is a number for remainder
def fibonacci(n, r):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, (a + b) % r
    return a


r = 10 ** 6 + 3
n = int(input())
x = fibonacci(n, r)
print(x)