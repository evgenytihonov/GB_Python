# 3.  Узнайте у пользователя число n.  Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.  Считаем 3 + 33 + 333 = 369.

print('Задание 3')

n = input('Введи число: ')

single = int(n)
double = int(n+n)
triple = int(n+n+n)

sum_n = single + double + triple

print(f'{single} + {double} + {triple} = {sum_n}')
