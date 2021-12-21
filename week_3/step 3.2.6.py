# Строкой Фибоначчи называется строка, состоящая только из 0 и 1, в которой не встречается двух 1 подряд.
# Вам требуется найти количество таких строк длины n.

def count_fib_str(n):
    if n == 0:
        return 1
    fib_str = [0] * (n + 1)
    fib_str[0] = 1
    fib_str[1] = 2

    for i in range(2, n + 1):
        fib_str[i] = fib_str[i - 1] + fib_str[i - 2]
    return fib_str[n]


n = int(input())
result = count_fib_str(n)
print(result)
