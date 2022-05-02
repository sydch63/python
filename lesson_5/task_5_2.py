def iterator_with_yield(numbers):
    sum_number = 0
    for number in range(1, numbers + 1, 2):
        if number ** 2 < 200:
            sum_number += number
            yield number,sum_number

gen1 = iterator_with_yield(30)

while True:
    print(next(gen1))
