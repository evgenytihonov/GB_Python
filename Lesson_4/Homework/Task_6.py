# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
#
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание,
# что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.

from itertools import count, cycle

print("Введите команду, чтобы выполнить итераторы.\r\n\nФорматы команд:" +
      "\r\n  -i=10,20\t- выведет последовательно 10 чисел, начиная с 20;" +
      "\r\n  -c=8\t\t- выведет последовательность из 8 чисел из цикла [1, 2, 3]." +
      "\r\nПосле выполнения введённой команды задание будет завершено.")
user_input = input("Команда? ")

if user_input.startswith("-i="):
    user_input = user_input.split("=")[1].split(",")
    numbers_count = user_input[0]
    numbers_count = int(numbers_count)
    numbers_start = user_input[1]
    numbers_start = int(numbers_start)
    counter = 0

    for num in count(numbers_start):
        counter += 1
        if numbers_count <= 0:
            break
        else:
            print(num, end="\r\n" if counter % 10 == 0 else " ")
            numbers_count -= 1

elif user_input.startswith("-c="):
    user_input = user_input.split("=")[1]
    numbers_count = int(user_input)
    counter = 0

    for num in cycle((1, 2, 3)):
        counter += 1
        if numbers_count <= 0:
            break
        else:
            print(num, end="\r\n" if counter % 10 == 0 else " ")
            numbers_count -= 1

else:
    print("Неизвестная команда. Вывод отменён")
