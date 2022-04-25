lst1 = [57.8, 46.40, 97, 12.3, 67.54, 8.07, 982.12, 100,228,11.5,3.58,4.70]
str1 = ''
rub = ' руб '
cop = ' коп, '
for index,element in enumerate(lst1):
    index_next = index + 1
    if isinstance(element,int) == True:
        new_element = str(element) + ' руб 00 коп'
        str1 += new_element + ', '
    else:
        new_element = str(element).split(".")
        if len(new_element[1]) > 1:
            str1 += new_element[0] + rub + new_element[1] + cop
        else:
            str1 += new_element[0] + rub + new_element[1] + '0' + cop

print('   Исходный список:')
print(lst1)
print(str1)
print('Доказательство операции in place:')
print("    id перед сортировкой: "+str(id(lst1)))
lst1.sort()
print("    id после сортировкой: "+str(id(lst1)))
print(lst1)

lst_new = [57.8, 46.40, 97, 12.3, 67.54, 8.07, 982.12, 100,228,11.5,3.58,4.70]
lst_new.sort(reverse=True)
print(lst_new)
print("ID нового списока: "+str(id(lst_new)))
price1,price2,price3,price4,price5 = lst_new[0:5]
print('5 самых дорогих товаров:\n' + f'    {str(price1)} \n    {str(price2)} \n    {str(price3)} \n    {str(price4)} \n    {str(price5)} \n')
