# 2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.

number_range = range(1,1001)
list_cubed = []
list_divided_7 = []
for number in number_range:
    if number % 2 != 0:
        number_cubed = number * (number**2)
        list_cubed.append(number_cubed)
for number in list_cubed:
    sum_number = 0
    number_finally = number
    while number // 10 != 0:
        number_remain = number % 10
        sum_number += number_remain
        number = number // 10
        if number // 10 == 0:
            sum_number += number
    if sum_number % 7 == 0 and sum_number != 0:
        list_divided_7.append(number_finally)
    sum_number_divided_7 = 0
for number in list_divided_7:
    sum_number_divided_7 += number
print("Сумма цифр деленных на 7:", sum_number_divided_7)
list_divided_7.clear()
for number in list_cubed:
    number += 17
    sum_number = 0
    number_finally = number
    while number // 10 != 0:
        number_remain = number % 10
        sum_number += number_remain
        number = number // 10
        if number // 10 == 0:
            sum_number += number
    if sum_number % 7 == 0 and sum_number != 0:
        list_divided_7.append(number_finally)
        sum_number_divided_7 = 0
for number in list_divided_7:
        sum_number_divided_7 += number
print("Сумма цифр деленных на 7:", sum_number_divided_7)