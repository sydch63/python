import sys

if len(sys.argv) == 1:
    print("Введите одно целое число")
elif sys.argv[1].isdigit() == True:
    if type(int(sys.argv[1])) == int:
        with open('bakery.csv', 'a',encoding='utf-8') as f:
            f.write(sys.argv[1] +'\n')
    else:
        print('Некорректный ввод данных, требуется вводить только целое число за раз')
else:
    print('Некорректный ввод данных, требуется вводить только целое число за раз')