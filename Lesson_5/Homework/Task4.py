import tools, os

user_input = input(
    "Введите набор целых положительных чисел, разделяя их пробелами (другие данные будут прогнорированы):\r\n> ")

numbers = [int(x) for x in user_input.split() if x.isdigit()]

file_path = os.path.join(tools.get_dir(), "lesson5_task4.txt")

with open(file_path, 'w') as stream:
    print(*numbers, file=stream)

print("Ваш массив данных размещён в файле:\r\n" + file_path)
print("Сумма введённых чисел: " + str(sum(numbers)))
tools.ask_to_read_file(file_path)
