# 20k20.
#
# Владислав заметил, что в 20202020-м году целых две пары одинаковых символов - 22 и 00.
# На основании этого он возненавидел цифры 22 и 00, а также ситуацию, когда в году есть одинаковые цифры.
# Сейчас Владислав ждет следующего года, в котором нет цифр 22 и 00, а также все цифры попарно различны.
# Посчитайте, в каком году это случится первый раз?

def is_consist_02(some_str):
    for i in range(len(some_str)):
        if some_str[i] == '2' or some_str[i] == '0':
            return True
    return False

def is_consist_2(some_str):
    for i in range(len(some_str)):
        if some_str[i] == '2':
            return True
    return False

def is_consist_0(some_str):
    for i in range(len(some_str)):
        if some_str[i] == '0':
            return True
    return False

def is_has_different_digit(some_str):
    if len(set(some_str)) < len(some_str):
        return False
    return True

def next_number_2(some_str):
    pos = -1
    new_some_str = ''
    if not is_consist_2(some_str):
        return int(some_str)
    else:
         for i in range(len(some_str)):
            if some_str[i] == '2':
                pos = i
                break
            new_some_str += some_str[i]

    new_some_str += '3'
    for i in range(pos + 1, len(some_str)):
        new_some_str += '0'
    return int(new_some_str)

def next_number_0(some_str):
    new_some_str = ''
    for i in range(len(some_str)):
        if some_str[i] == '0':
            new_some_str += '1'
        else:
            new_some_str += some_str[i]
    return int(new_some_str)

n = int(input())
n += 1
n = next_number_2(str(n))
max_n = 98765431
isFounded = False

if n > max_n:
    print(-1)
else:
    while n < max_n + 1:
        if is_consist_2(str(n)):
            n = next_number_2(str(n))
        if is_consist_0(str(n)):
            n = next_number_0(str(n))

        if is_has_different_digit(str(n)) and not is_consist_02(str(n)):
            print(n)
            isFounded = True
            break
        n += 1

    if not isFounded:
        print(-1)
