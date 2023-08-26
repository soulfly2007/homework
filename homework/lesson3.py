# Задачи для домашней работы

# •	Найти самое длинное слово в введенном предложении. Учтите что в предложении есть знаки препинания.
s = input('Enter a string: ')
s = [a.strip(",.:;!?") for a in s.split()]
print(max(s, key=len))

# •	Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
# Например, если было введено "abc cde def", то должно быть выведено "abcdef".
# s ='abc cde def'
s = input('Enter a string: ')
print(''.join(dict.fromkeys(s.replace(' ', ''))))

# •	Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
# Учитывать только английские буквы.
# s ='abc CDE def АБВ'
s = input('Enter a string: ')
low_case_letter = 0
upper_case_letter = 0
for i in s:
    if 'a' <= i <= 'z':
        low_case_letter += 1
    elif 'A' <= i <= 'Z':
        upper_case_letter += 1
print('low_case_letter =', low_case_letter)
print('upper_case_letter =', upper_case_letter)
