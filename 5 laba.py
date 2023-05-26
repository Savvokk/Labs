def n1():
    n = 0
    sp = {"Россия": "Москва", "Великобритания": "Лондон", "США": "Вашингтон", "Германия": "Берлин",
          "Бельгия": "Брюссель"}
    print(sp)

    while n != 1:
        capital = input("Введите страну: ")
        if capital in sp.keys():
            print("Столица этой страны: ", sp[capital])
            n = 1
        else:
            print("Такой страны нет в базе данных")

    sp = sorted(sp.items(), key=lambda x: x[0])
    print(sp)


def n2():
    sp = {"а": 1, "в": 1, "е": 1, "и": 1, "н": 1, "о": 1, "р": 1, "с": 1, "т": 1, "д": 2, "к": 2, "л": 2, "м": 2,
          "п": 2, "у": 2, "б": 3, "г": 3, "ё": 3, "ь": 3, "я": 3, "й": 4, "ы": 4, "ж": 5, "з": 5, "х": 5, "ц": 5,
          "ч": 5, "ш": 8, "э": 8, "ю": 8, "ф": 10, "щ": 10, "ъ": 10}
    word = input("Введите слово: ")
    k = 0
    for i in word:
        k += sp[i.lower()]
    print('Сумма очков = ', k)


def n3():
    le = ['русский', 'английский', 'китайский']
    sp = {'русский': ['денисов', 'яриз', 'банбасов', 'логинов', 'вдовичева'],
          'английский': ['денисов', 'яриз', 'банбасов', 'логинов', 'вдовичева'],
          'китайский': ['денисов', 'яриз', 'шань', 'ибин', 'хаовей']}
    le.sort()
    s = len(le)
    print('Количество языков - ', s)
    print('Список по алфавиту - ', le)
    print('Введите любой язык из списка', le)
    a = str(input())
    print(sp[a])


n1()
n2()
n3()