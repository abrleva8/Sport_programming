# Во входном файле задано целое число N, не превосходящее 10^9.
# Найдите остаток от деления числа N!N!  (произведения всех чисел от 1 до N) на 10^6+3.


def find_answer(n):
    result = 1
    remainder = 10 ** 6 + 3
    if n >= remainder:
        return 0
    for i in reversed(range(1, n + 1)):
        result = (result * (i % remainder)) % remainder
    return result


n = int(input())
result = find_answer(n)
print(result)
