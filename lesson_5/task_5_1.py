def iterator_without_yield(numbers):
       gen = (number for number in range(1,numbers+1) if number % 2 != 0 and number**2 < 200)
       return gen

gen1 = iterator_without_yield(30)

while True:
    print(next(gen1))