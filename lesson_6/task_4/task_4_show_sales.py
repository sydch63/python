import sys

with open('bakery.csv','r',encoding='utf-8') as f:
    lst_price = f.read().split('\n')
    lst_price.pop(len(lst_price)-1)
    if len(sys.argv) == 1:
        for el in lst_price:
            print(el)
    elif len(sys.argv) == 2 and sys.argv[1].isdigit() and int(sys.argv[1]) <= len(lst_price):
        if type(int(sys.argv[1])) == int:
            for el in lst_price[int(sys.argv[1])-1::]:
                print(el)
        else:
            print('Некорректный ввод данных')
    elif len(sys.argv) == 3 and (sys.argv[1].isdigit() and sys.argv[2].isdigit()) and int(sys.argv[1]) <= len(lst_price) and int(sys.argv[1]) <= int(sys.argv[2]) :
        if type(int(sys.argv[1])) == int:
            for el in lst_price[int(sys.argv[1])-1:int(sys.argv[2])]:
                print(el)
        else:
            print('Некорректный ввод данных')
    else:
        print('Некорректный ввод данных')