# Имеется калькулятор, который выполняет следующие операции:
# Умножить число X на 2.
# Умножить число X на 3.
# Прибавить к числу X единицу.
# Определите, какое наименьшее количество операций требуется, чтобы получить из числа 1 число N.

def find_answer(n):
    if n == 1:
        return 0
    dp_array = [0] * (n + 2)
    for i in range(2, n + 1):
        if i % 6 == 0:
            dp_array[i] = min(dp_array[i // 3], dp_array[i // 2], dp_array[i - 1]) + 1
        elif i % 3 == 0:
            dp_array[i] = min(dp_array[i // 3], dp_array[i - 1]) + 1
        elif i % 2 == 0:
            dp_array[i] = min(dp_array[i // 2], dp_array[i - 1]) + 1
        else:
            dp_array[i] = dp_array[i - 1] + 1
    return dp_array[n]

n = int(input())
result = find_answer(n)
print(result)
