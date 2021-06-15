# Коровы в стойла

# На прямой расположены стойла, в которые необходимо расставить коров так,
# чтобы минимальное растояние между коровами было как можно больше.


# @arr is list; x, count are int number
# the method checks might be @x the distance between cows, or not
def check(arr, x, count):
    it = 0
    next_it = 1
    my_count = 1
    while next_it < len(arr):
        # print(next_it)
        if arr[next_it] - arr[it] < x:
            next_it = next_it + 1
        else:
            my_count = my_count + 1
            it = next_it
            next_it = next_it + 1
    return my_count >= count


def find_answer(arr, count):
    left = 0
    right = arr[-1]
    while left + 1 < right:
        mid = (left + right) // 2
        if check(arr, mid, count):
            left = mid
        else:
            right = mid
    return left


n, k = map(int, input().split())
arr = [int(i) for i in input().split()]

result = find_answer(arr, k)
print(result)

