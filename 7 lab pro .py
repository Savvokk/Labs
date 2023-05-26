def n1():
    word = input("Введите слово")
    if 'ф' in word or 'Ф' in word:
        print(word, '-Ого! Это очень редкое слово!')
    else:
        print(word, 'Эх, это не очень редкое слово...')


def n2():
    import random
    k = 0
    while k < 3:
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        print(a, '+', b, '=')
        res = int(input("Введите ответ:"))
        if res == a + b:
            print('Правильно!')
        else:
            print('Неправильно!')
            k += 1
    else:
        print('Игра закончена')


n1()
n2()