# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

user_input = input("Введите несколько слов, разделённых пробелами:")
n = 1
for part in user_input.split(' '):
    print(f'{n}. {part[0:10] if len(part) > 10 else part}')
    n += 1