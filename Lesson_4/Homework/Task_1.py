# Реализовать скрипт, в котором должна быть предусмотрена
# функция расчета заработной платы сотрудника. В расчете необходимо
# использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо
# запускать скрипт с параметрами.

def sal():
    try:
        time = float(input('Введите количество отработанных часов: '))
        salary = int(input('Введите ставку за час в у.е.: '))
        bonus = int(input('Введите премию в у.е.: '))
        res = time * salary + bonus
        print(f'Заработная плата сотрудника составляет: {res}')
    except ValueError:
        return print('Not a number')
sal()