# Перед клетчатой полоской длины n сидит кузнечик. В каждой клетке написано целое число.
# Когда кузнечик оказывается в какой-то клетке, ему дают конфет в том количестве, которое записано в этой клетке.
# Кузнечик умеет прыгать на следующую ступеньку, а также через одну.Помогите кузнечику - определите,
# какое максимальное количество конфет он может съесть, если в итоге кузнечик должен оказаться в последней клетке?
# Обратите внимание, количество конфет может быть отрицательно.

# arr is array with integer numbers
def find_answer(arr):
    size = len(arr)
    dp_array = [0] * (size + 1)
    dp_array[1] = arr[0]
    for i in range(1, size):
        dp_array[i + 1] = max(dp_array[i], dp_array[i-1]) + arr[i]
    return dp_array

n = int(input())
arr = [int(i) for i in input().split()]
# result_arr has @(n+1) number
result_arr = find_answer(arr)
result = result_arr[n]
print(result)
