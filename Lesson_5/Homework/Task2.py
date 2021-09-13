import os
import re
import tools

path = tools.get_dir("lesson5_data")
if path is None:
    print("Директория с данными не обнаружена. Проверьте, что Вы загрузили все файлы проекта.")

path = os.path.join(path, "task2_data.txt")
if not os.path.exists(path) or not os.path.isfile(path):
    print("Файл с данным для этого задания не обнаружен.\r\n" + path +
          "\r\nПроверьте, что Вы загрузили все файлы проекта.")

strings = []

try:
    with open(path) as stream:
        strings = stream.readlines()
except:
    print("Ошибка чтения файла")

# Теперь немного "магии одной строки".
# Следующая команда последовательно:
# - берёт каждую прочитанную строку, если она пустая, то пропускает её, а для остальных:
#       - удаляет пробельные символы в начале и конце строки;
#       - удаляет все символы, не являющиеся пробельными либо буквами латиницы и кириллицы;
#       - из полученной строки удаляет задублированные пробелы. Они могут появляться, после
#           предыдущей команды при удалении тире ('_-_' -> '__');
#       - считает количество пробелов, разделяющих слова, и добавляет единицу - это количество слов;
#       - добавляет полученную строку в перечисление кортежей, где первую часть занимает посчитанное количество слов,
#           а во второй части находится исходная строка;
# - сформированное перечисление кортежей пронумировывает (начиная со значения 1) и передаёт в словарь, где
#     ключом выступает номер строки, а значением - вышеуказанный кортеж из строки и количества слов в этой;
magic = {string_num: line for string_num, line
         in enumerate(((re.sub(r"[^a-zA-ZА-Яа-я\s]", '', line.strip()).replace('  ', ' ').count(' ') + 1, line)
                       for line in strings if not line.isspace() and line != ''), start=1)}

# осталось только красиво вывести на экран
print("Стр.№", "Кол.", "Строка", sep="\t| ")
print('-' * 30)
for key, value in magic.items():
    print(key, value[0], value[1].replace("\n", ''), sep="\t| ")