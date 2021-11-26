# КузнечиК
#
# Перед клетчатой полоской длины n сидит кузнечик. Каждая клетка является либо занятой, либо свободной.
# Кузнечик умеет прыгать на 1, 2... k клеток вперед. Найдите количество различных путей,
# которыми он может добраться до последней клетки, не заходя в занятые.

def find_answer(arr_str, step, mod_p):
    size = len(arr_str)
    sum_array = [0] * (size + 1)
    sum_array[0] = 1
    s = 0

    for i in range(1, step + 1):
        if arr_str[i - 1] == '1':
            sum_array[i] = 0
        else:
            sum_array[i] += (s + 1)
            s = (s + sum_array[i]) % mod_p

    for i in range(step + 1, size + 1):
        j = i - step
        if arr_str[i - 1] == '1':
            sum_array[i] = 0
        else:
            # print('i = ' + str(i) + ' j = ' + str(j))
            sum_array[i] = s
            s = (s + sum_array[i]) % mod_p
        s = (s - sum_array[j]) % mod_p
    return sum_array[size]


n, step = map(int, input().split())
string = input()
mod_p = 10 ** 9 + 7
result = find_answer(string, step, mod_p)
print(result)
