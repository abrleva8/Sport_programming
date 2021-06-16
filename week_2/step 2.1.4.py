# Задано целое число N (4 <=N <= 10^6)
# Найти сумму наименьших простых делителей всех составных чисел, больших 2 и не превосходящих N.


def incognito(n):
    _result = 0
    arr = [0] * (n + 1)
    i = 2
    while i * i <= n + 2:
        if arr[i] == 0:
            j = i
            while j * i <= n:
                if arr[i * j] == 0:
                    arr[i * j] = 1
                    _result = _result + i
                j = j + 1
        i = i + 1
    return _result


n = int(input())
result = incognito(n)
print(result)
