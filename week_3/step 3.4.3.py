# Имеется калькулятор, который выполняет следующие операции:
#
# Умножить число X на 2.
# Умножить число X на 3.
# Прибавить к числу X единицу.
# Определите, какое наименьшее количество операций требуется, чтобы получить из числа 1 число N.

def find_answer(n):
    if n == 1:
        return [1]
    dp_array = [0] * (n + 2)
    path = []
    for i in range(2, n + 1):
        if i % 6 == 0:
            dp_array[i] = min(dp_array[i // 3], dp_array[i // 2], dp_array[i - 1]) + 1
        elif i % 3 == 0:
            dp_array[i] = min(dp_array[i // 3], dp_array[i - 1]) + 1
        elif i % 2 == 0:
            dp_array[i] = min(dp_array[i // 2], dp_array[i - 1]) + 1
        else:
            dp_array[i] = dp_array[i - 1] + 1

    x = n
    while x > 1:
        path.append(x)
        if dp_array[x - 1] == dp_array[x] - 1:
            x -= 1
        elif x % 2 == 0 and dp_array[x // 2] == dp_array[x] - 1:
            x //= 2
        else:
            x //= 3
    path.append(1)
    return path


n = int(input())
result = find_answer(n)
print(len(result) - 1)
print(*reversed(result))
