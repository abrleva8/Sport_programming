# Очень легкая задача

# Сегодня утром жюри решило добавить в вариант олимпиады еще одну, Очень Легкую Задачу.
# Ответственный секретарь Оргкомитета напечатал ее условие в одном экземпляре, и теперь ему нужно до начала олимпиады
# успеть сделать еще NN копий. В его распоряжении имеются два ксерокса, один из которых копирует лист за х секунд,
# а другой – за y. (Разрешается использовать как один ксерокс, так и оба одновременно.
# Можно копировать не только с оригинала, но и с копии.) Помогите ему выяснить,
# какое минимальное время для этого потребуется.


def find_answer(N, x, y):
    if x > y:
        x, y = y, x
    N = N - 1
    left = 0
    right = N * x
    while left + 1 < right:
        mid = (left + right)//2
        count_1 = mid//x
        count_2 = mid//y
        if count_1 + count_2 < N:
            left = mid
        else:
            right = mid
    return right + x


N, x, y = map(int, input().split())

result = find_answer(N, x, y)

print(result)
