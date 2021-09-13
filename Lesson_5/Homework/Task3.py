import os
import tools


def run():
    # Часть 1 - Зарплата сотрудников
    print("Часть 1 - Зарплата сотрудников")
    directory = tools.get_dir("lesson_5_data")

    if directory is None:
        print("Директория с данными не обнаружена. Проверьте, что Вы загрузили все файлы проекта.")
        return

    file = os.path.join(directory, "task3a_data.txt")
    if not os.path.exists(file) or not os.path.isfile(file):
        print("Файл с указанным именем не обнаружен, либо не является файлом." +
              "Проверьте, что Вы загрузили все файлы проекта.")
        return

    strings = []
    try:
        with open(file) as stream:
            strings = stream.readlines()
    except:
        print("Ошибка чтения файла")
        return

    persons = {line.split(' ')[0]: float(line.split(' ')[1]) for line in strings if line != ''}

    print("Оклад меньше 20 тыс. у следующих сотрудников: ",
          *[person for person in persons.keys() if persons[person] < 20_000])
    print("Средняя заработная плата: " + str(round(sum(persons.values()) / len(persons), 2)))

    # Часть 2 - Числительные
    print("Часть 2 - Числительные")

    dictionary = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре", "Five": "Пять", "Six": "Шесть",
                  "Seven": "Семь", "Eight": "Восемь", "Nine": "Девять", "Zero": "Ноль"}

    in_file = os.path.join(directory, "task3b_data.txt")
    if not os.path.exists(file) or not os.path.isfile(file):
        print("Файл с указанным именем не обнаружен, либо не является файлом." +
              "Проверьте, что Вы загрузили все файлы проекта.")
        return

    directory = tools.get_dir()
    if directory is None:
        print("Ошибка создания директории для хранения новых фалов.")
        return

    out_file = os.path.join(directory, "lesson5_task3.txt")
    try:
        with open(in_file) as in_stream:
            with open(out_file, 'w') as out_stream:
                while True:
                    line = in_stream.readline()
                    if not line:
                        break
                    word_to_replace = line.split('-')[0].strip()
                    out_stream.write(line.replace(word_to_replace, dictionary[word_to_replace]))
    except BaseException as ex:
        print("Ошибка чтения или записи файлов", ex)
        return

    print("Новый файл с переводом опубликован по следующему пути\r\n" + out_file)
    tools.ask_to_read_file(out_file)


run()
