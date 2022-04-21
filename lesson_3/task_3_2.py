# 2. [Задача со звездочкой]: усложненный вариант задания 1. Написать функцию num_translate_adv, которая корректно обработает числительные, начинающиеся с заглавной буквы.
# Если перевод сделать невозможно, вернуть объект None.
# Условие задачи
# Техническое задание
#
# Функция возвращает строку перевод. Или возвращает None, если перевести невозможно.
# Считаем, что только первая буква может быть заглавной.
# Обратите внимание, что функция возвращает перевод в том же регистре как и приняла.
# Выполнить вызов функции для нескольких слов и вывести на экран результаты.
# Примеры/Тесты:
#
#
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

dct_eng_rus = {"one":"один","two":"два","three":"три","four":"четыре","five":"пять","six":"шесть","seven":"семь","eight":"восемь","nine":"девять","ten":"десять"}

def num_translate(word):
    if word.istitle() is True:
        word = word.lower()
        return print(dct_eng_rus.get(word).capitalize())
    else:
        word = word.lower()
        return print(dct_eng_rus.get(word))


num_translate("One")
num_translate("5")
num_translate("eleven")
num_translate("Five")
num_translate("six")