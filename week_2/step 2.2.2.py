# Во входном файле заданы два  неотрицательных целых числа a и b, не превосходящие 10^5.
# Вычислите остаток от деления разности a^2-b^2 на 10^6+7.


def find_answer(a, b):
    d = a - b
    s = a + b
    remainder = 10 ** 6 + 7
    result = (d * s) % remainder
    return result


a, b = map(int, input().split())
result = find_answer(a, b)
print(result)
