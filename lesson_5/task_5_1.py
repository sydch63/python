def iterator_with_yield(numbers):
   gen = (number for number in range(1,numbers+1,2) if number**2 < 200)
   return gen

gen1 = iterator_with_yield(30)

while True:
    print(next(gen1))