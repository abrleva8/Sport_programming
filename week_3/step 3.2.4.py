# Перед клетчатой полоской длины n сидит кузнечик. Каждая клетка является либо занятой, либо свободной.
# Кузнечик умеет прыгать на 1, 2 и 3 клетки вперед. Найдите количество различных путей, которыми он может добраться
# до последней клетки, не заходя в занятые.

# @arr_str is string which filled with '0' and '1'
# @mod_p - is prime number.
def find_answer(arr_str, mod_p=10**9 + 7):
    size = len(arr_str)
    arr = [0] * (size + 1)
    arr[0] = 1
    for i in range(1, size + 1):
        if arr_str[i - 1] == '1':
            arr[i] = 0
        else:
            arr[i] = sum(arr[max(0, i - 3): i]) % mod_p
    return arr[size]

n, string = int(input()), input()
result = find_answer(string)
print(result)
