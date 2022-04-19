# Для всех нечетных чисел диапазона [1, 1000]
# вычислить их куб
# вычислить сумму цифр куба
# если сумма цифр куба делится нацело на 7, то добавить в накопительную сумму исходное число.
# При решении задачи использовать только арифметические операции и цикл while.
# Не используем списки, функцию range, преобразование числа в строку/список.
# Ваш алгоритм должен корректно работать для всех чисел интервала от 1 до 1000, но и легко изменяться для другого диапазона чисел, например от 1 до 10000000.

number = 1
sum_all_number_divided_7 = 0
while number != 1001:
    if number % 2 != 0:
        number_cubed = number * (number ** 2)
        sum_number = 0
        while number_cubed // 10 != 0:
            number_remain = number_cubed % 10
            sum_number += number_remain
            number_cubed = number_cubed // 10
            if number_cubed // 10 == 0:
                sum_number += number_cubed
                if sum_number % 7 == 0 and sum_number !=0:
                    sum_all_number_divided_7 += number
                    print(number,"^3= ",number_cubed,"[",sum_number,"]",'накоп. сумма:',sum_all_number_divided_7)
        else:
            number += 1
    else:
        number += 1
