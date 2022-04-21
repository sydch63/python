lst =  ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

print ("Обычный вариант")
print ("")
for element in lst:
    lst_new = element.split(" ")
    name = lst_new[::-1][0].capitalize()
    print(f"Привет,{name}!")

print ("")
print ("Усложненый вариант")
print ("")
for element in lst:
    lst_new = element.split(" ")
    name = lst_new[::-1][0]
    post = lst_new[0:lst_new.index(name)]
    post = " ".join(lst_new[0:lst_new.index(name)])
    name = lst_new[::-1][0].capitalize()
    print(f"Привет,{post} {name}!")