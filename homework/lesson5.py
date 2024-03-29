# Задачи для домашней работы
# Пары элементов
# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# Входные данные - строка из чисел, разделенная пробелами.
# Выходные данные - количество пар. Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар.
a = [int(i) for i in input().split()]
num_dict = {}
for i in a:
    num_dict[i] = num_dict.get(i, 0) + 1
print(sum(v * (v - 1) // 2 for v in num_dict.values()))

# Уникальные элементы в списке
# Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
# Элементы нужно выводить в том порядке, в котором они встречаются в списке.
a = [1, 2, 1, 2, 3, 4]
unique = {}
for i in a:
    unique[i] = unique.get(i, 0) + 1
print([k for k, v in unique.items() if v == 1])

# Упорядоченный список
# Дан список целых чисел. Требуется переместить все ненулевые элементы в левую часть списка,
# не меняя их порядок, а все нули - в правую часть.
# Порядок ненулевых элементов изменять нельзя, дополнительный список использовать нельзя,
# задачу нужно выполнить за один проход по списку.
# Распечатайте полученный список.
lst.sort(key=lambda i: i == 0)
print(lst)

# Задачи для домашней работы
# Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
lst = ['a', 'b', 'c']
tpl = tuple(lst)

# Создайте кортеж ('a', 'b', 'c'), И сделайте из него список.
tpl = 'a', 'b', 'c'
lst = list(tpl)

# Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
a, b, c = 'a', 2, 'python'

# Создайте кортеж из одного элемента,
# чтобы при итерировании по этому элементу последовательно выводились значения 1, 2, 3.
# Убедитесь что len() исходного кортежа возвращает 1.
tpl = (1, 2, 3),
print(len(tpl))
for i in tpl[0]:
    print(i, end=' ')

# Даны два натуральных числа.
# Вычислите их наибольший общий делитель при помощи алгоритма Евклида (мы не знаем функции и рекурсию).
a, b = map(int, input().split())
while b > 0:
    a, b = b, a % b
print(a)

# Задачи для домашней работы
# *Города*
# Дан список стран и городов каждой страны. Затем даны названия городов.
# Для каждого города укажите, в какой стране он находится.
# Учтите, что бывают ситуации когда город с таким называнием бывает в разных странах (Брест есть в Беларуси и Франции).
# Входные данные
# Программа получает на вход количество стран N.
# Далее идет N строк, каждая строка начинается с названия страны,
# затем идут названия городов этой страны.
# В следующей строке записано число M, далее идут M запросов — названия каких-то M городов, перечисленных выше.
# Выходные данные
# Для каждого из запроса выведите название страны, в котором находится данный город.
# Пример данных:
# Входные данные
# 2
# Russia Moscow Petersburg Novgorod Kaluga
# Ukraine Kiev Donetsk Odessa
# 3
# Odessa
# Moscow
# Novgorod
# Выходные данные
# Ukraine
# Russia
# Russia
cities_countries = {}
for _ in range(int(input())):
    country, *cities = input().split()
    for city in cities:
        cities_countries.setdefault(city, []).append(country)
for _ in range(int(input())):
    print(*cities_countries[input()])

# Задачи для домашней работы
# Во входной строке записан текст.
# Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца строки.
# Определите, сколько различных слов содержится в этом тексте.
print(len(set(s.split())))

# Даны два списка чисел.
# Посчитайте, сколько различных чисел содержится одновременно как в первом списке, так и во втором.
print(len(set(lst) ^ set(lst1)))

# Даны два списка чисел. Посчитайте, сколько различных чисел входит только в один из этих списков.
print(len(set(lst) - set(lst1)))

# *Языки*
# Каждый из N школьников некоторой школы знает Mi языков.
# Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
# Входные данные
# Первая строка входных данных содержит количество школьников N.
# Далее идет N чисел Mi, после каждого из чисел идет Mi строк, содержащих названия языков, которые знает i-й школьник.
# Пример входных данных:
# 3 # N количество школьников
# 2 # M1 количество языков первого школьника
# Russian # языки первого школьника
# English
# 3 # M2 количество языков второго школьника
# Russian
# Belarusian
# English
# 3
# Russian
# Italian
# French
# *Выходные данные*
# В первой строке выведите количество языков, которые знают все школьники.
# Начиная со второй строки - список таких языков.
# Затем - количество языков, которые знает хотя бы один школьник, на следующих строках - список таких языков.
known_every = set()
known_some = set()
for i in range(int(input())):
    langs = {input() for _ in range(int(input()))}
    known_some.update(langs)
    if len(known_every) == 0:
        known_every.update(langs)
    else:
        known_every.intersection_update(langs)
print(len(known_every), *known_every, len(known_some), *known_some, sep='\n')

# Задачи для домашней работы
# Генераторы списков
# Используйте генератор списков чтобы получить следующий: ['xy', 'xz', 'xv', 'yy', 'yz', 'yv'].
lst = [el + el1 for el in 'xy' for el1 in 'yzv']

# Используйте на предыдущий список slice чтобы получить следующий: ['xy', 'xv', 'yz'].
lst[::2]

# Используйте генератор списков чтобы получить следующий ['1x', '2x', '3x', '4x'].
lst = [str(i) + 'x' for i in range(1, 5)]

# Одной строкой (и одним выражением) удалите элемент '2x' из прошлого списка и напечатайте его.
print(lst.pop(1))

# Скопируйте список и добавьте в него элемент 2x так чтобы в исходном списке этого элемента не было.
lst1 = lst.copy() + ['2x']
print(lst1)

# Генераторы словарей
# Создайте словарь с помощью генератора словарей,
# так чтобы его ключами были числа от 1 до 20, а значениями кубы этих чисел.
{i: i ** 3 for i in range(1, 21)}

# Генераторы множеств
# Создайте множество с помощью генератора множеств, состоящее из общих делителей чисел 1000 и 9000.
{i for i in range(1, 1000 + 1) if 1000 % i == 0 and 9000 % i == 0}

# Задача для домашней работы
# Создайте генератор, который возвращает строки таблицы умножения от 0 до заданного числа.
def get_mult_table(n):
    for i in range(n + 1):
        yield '\t'.join(str(i * j) for j in range(n + 1))


n = int(input('Enter an integer: '))
for i in get_mult_table(n):
    print(i)
