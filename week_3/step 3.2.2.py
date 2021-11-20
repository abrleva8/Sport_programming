# Перед клетчатой полоской длины nn сидит кузнечик. В каждой клетке написано целое число.
# Когда кузнечик оказывается в какой-то клетке, ему дают конфет в том количестве, которое записано в этой клетке.
# Кузнечик умеет прыгать на следующую ступеньку, через две и через четыре ступеньки.
# То есть, если кузнечик сидит в клетке с номером i, то за один шаг он может оказаться в клетках с номерами
# i + 1, i + 3 i + 5. Помогите кузнечику - определите, какое максимальное количество конфет он может съесть,
# если в итоге он должен оказаться в последней клетке? Обратите внимание, количество конфет может быть отрицательно.

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
    return dp_array


n = int(input())
arr = [int(i) for i in input().split()]
# result_arr has @(n+1) number
result_arr = find_answer(arr)
result = result_arr[n]
print(result)
