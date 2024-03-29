# Задачи для домашней работы
# Выведите n-ое число Фибоначчи, используя только временные переменные, циклические операторы и условные операторы.
# n - вводится.
n = int(input())
if n <= 2:
    print(n - 1)
else:
    fib1 = 0
    fib2 = 1
    while n > 2:
        fib1, fib2 = fib2, fib1 + fib2
        n -= 1
    print(fib2)

# Определите, является ли число палиндромом (читается слева направо и справа налево одинаково).
# Число положительное целое, произвольной длины.
# Задача требует работать только с числами (без конвертации числа в строку или что-нибудь еще).
n = int(input())
n1 = n
m = 0
while n != 0:
    i = n % 10
    m = m * 10 + i
    n = n // 10
if m == n1:
    print('Palindrome')
else:
    print('Not Palindrome')

# Напишите программу, которая печатает цифры от 1 до 100,
# но вместо чисел, кратных 3 пишет Fizz,
# вместо чисел кратный 5 пишет Buzz, а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz.
print(*['FizzBuzz' if i % 15 == 0 else 'Fizz' if i % 3 == 0 else 'Buzz' if i % 5 == 0 else i for i in range(1, 101)])
