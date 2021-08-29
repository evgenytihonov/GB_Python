# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

a = input('Введите первое число: ')
b = input('Введите второе число: ')
c = input('Введите третье число: ')
array = []
def my_func(*args):
    array = [*args]
    max1 = max(array)
    array.remove(max1)
    max2 = max(array)
    return max1, max2

print(f'Два максимальных значения: {my_func(a, b, c)}')