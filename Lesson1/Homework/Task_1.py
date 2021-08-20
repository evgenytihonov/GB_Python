# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите
# у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

print('Задание 1')

username = input('Введи имя: ')
age = abs(int(input('Введи возраст: ')))

print(f'\nЗдравствуйте, {username}.\n')

if age <= 18:
    print(f'\nПоздравляю, тебе {age} ты молод, всё впереди!\n')
else:
    print(f'{age}!!! Офигеть, жизнь подходит к концу, поторопись!')

height = abs(float(input('Введи рост в метрах: ')))

if height >= 1.6 and age > 22:
    print(f'\nПоздравляю, {username}, видимо, ты ел достаточно каши! {age}, как никак!\n')
elif height >= 1.6 and age <= 22:
    print(f'\nПоздравляю, {username}, видимо, ты ел достаточно каши! {age}, как никак!\n')
elif age <= 22:
    print(f'{height} нуу, не переживай, ты еще можешь вырости!')
else:
    print(f'{username} {age} полных отроду, {height}м.... генетику не выбирают')

check = bool(input('У тебя есть права (True/False)? '))

if check == True and age >= 18:
    print('Молодчик!')
elif check == False and age >= 18:
    print('Нужная штука!')
else:
    print('Не может быть такого!!!')
