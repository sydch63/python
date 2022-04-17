# Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на
# экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
# 1 процент
# 2 процента
# 3 процента
# 4 процента
# 5 процентов
# 6 процентов
# ...
# 100 процентов

number = 1
while number != 201:
    if number % 10 == 1 and number != 11 and number != 111:
        print(number, "процент")
        number += 1
    elif 5 <= number % 10 <= 9 or 11 <= number % 100 <= 14 or number % 10 == 0 or 111 <= number % 100 <= 114:
        print(number, "процентов")
        number += 1
    elif 2 <= number % 10 <= 4:
        print(number, "процента")
        number += 1
    else:
        number += 1
