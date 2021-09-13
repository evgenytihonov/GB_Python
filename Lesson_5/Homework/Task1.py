import os, tools

user_input = input("Начните вводить данные. Пустой ввод - отмена (завершение) ввода." +
                   "Запись в файл произойдёт после завершения ввода.\r\n> ")
strings = []

while user_input != '' and not user_input.isspace():
    strings.append(user_input + "\n")
    user_input = input("> ")

file_path = os.path.join(tools.get_dir(), "lesson5_task1.txt")

try:
    with open(file_path, 'wt') as stream:
        stream.writelines(strings)
except:
    print("Ошибка записи в файл")


print("Запись в файл успешна.", end=" ")
tools.ask_to_read_file(file_path)
