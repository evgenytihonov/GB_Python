# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
# и возвращающую его же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.

# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().
def run():
    while True:
        user_input = input("Введите несколько слов через пробел (пустой ввод - выход): ")

        if user_input == "" or user_input.isspace():
            print("Ввод завершён.")
            break

        for word in user_input.split():
            print(int_func(word), end=" ")
        print()

def int_func(word):
    """Возвращает строку, первая буква которой заменена на заглавную. Вернёт None, если получит не строку или пустую строку.
    :param word: строка, воспринимаемая как одно слово, подлежащая изменению -> str
    :return: строка с первой буквой, заменённой на заглавную."""

    if type(word) != str or word == "":
        return None

    return str(word).capitalize();

run()