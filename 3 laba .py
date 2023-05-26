def n1():
    number = int(input("Введите число"))
    if number % 3 == 0:
        print("делится на 3")
    else:
        print("не делится на 3")


def n2():
    res = None
    try:
        number = int(input('Введите число'))
        res = 100 / number
    except ValueError:
        print("Можно вводить только число")
    except ZeroDivisionError:
        print("На ноль делить нельзя")
    except Exception as e:
        print("Ошибка: ", e)
    print(res)


def n3():
    date = input('Введите дату dd/mm/yy:')
    try:
        date = date.split(".")
        if int(date[0]) * int(date[1]) == int(date[2][2:]):
            print('Дата магическая')
        else:
            print('Дата обычная')
    except:
        print("Дата вводится в формате dd.mm.yy")


def n4():
    ticket = int(input('введите номер билета'))
    sum1 = 0
    sum2 = 0
    for i in range(6):
        if i < 3:
            sum1 += ticket // 10 ** i % 10
        else:
            sum2 += ticket // 10 ** i % 10
    if sum1 == sum2:
        print('билет счастливый')
    else:
        print('билет несчастливый')


n1()
n2()
n3()
n4()