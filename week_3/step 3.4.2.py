# Перед клетчатой полоской длины nn сидит кузнечик. В каждой клетке написано целое число.
# Когда кузнечик оказывается в какой-то клетке, ему дают конфет в том количестве, которое записано в этой клетке.
# Кузнечик умеет прыгать на следующую ступеньку, через две и через четыре ступеньки.
# То есть, если кузнечик сидит в клетке с номером i, то за один шаг он может оказаться в клетках с номерами
# i + 1, i + 3, i + 5. Помогите кузнечику - определите, какое максимальное количество конфет он может съесть,
# если в итоге должен оказаться в последней клетке? Обратите внимание, количество конфет может быть отрицательно.

# arr is array with integer numbers
def find_answer(arr):
    size = len(arr)
    dp_array = [0] * (size + 1)
    dp_array[1] = arr[0]

    for i in range(1, size):
        if i < 2:
            dp_array[i + 1] = dp_array[i] + arr[i]
        elif i < 4:
            dp_array[i + 1] = max(dp_array[i], dp_array[i - 2]) + arr[i]
        else:
            dp_array[i + 1] = max(dp_array[i], dp_array[i - 2], dp_array[i - 4]) + arr[i]
    path = []
    current_pos = size
    while current_pos > 0:
        path.append(current_pos)
        if dp_array[current_pos - 1] + arr[current_pos - 1] == dp_array[current_pos]:
            current_pos -= 1
        elif dp_array[current_pos - 3] + arr[current_pos - 1] == dp_array[current_pos]:
            current_pos -= 3
        else:
            current_pos -= 5
    path.append(dp_array[size])
    return path


n = int(input())
arr = [int(i) for i in input().split()]
result = find_answer(arr)  # result_arr has @(n+1) number
print(result[-1], len(result) - 1)
for i in reversed(range(len(result) - 1)):
    print(result[i], end=' ')
