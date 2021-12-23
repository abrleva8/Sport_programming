# Найдите, сколько существует строк заданной длины n, состоящих только из символов a,b,c, и не содержащих подстроки ab

def find_answer(n):
    prev, curr = 0, 1

    for _ in range(n):
        prev, curr = curr, 3 * curr - prev
    return curr

n = int(input())
result = find_answer(n)
print(result)
