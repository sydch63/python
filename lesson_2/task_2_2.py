test1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
test2 = ['примерно в', '23', 'часа', '8', 'минут', '03', 'секунд', 'температура', 'воздуха', 'была', '-5', 'градусов Цельсия', 'темп', 'воды', '+12', 'градусов', 'Цельсия']
test3 = ['+9', 'примерно в', '23', 'часа', '8', 'минут', '03', '05', 'секунд', 'температура', 'воздуха', 'была', '5', 'градусов Цельсия', 'темп','воды','+2.0','градусов','Цельсия' ,'-2', '11']
lst1 = test3
quotation_mark = '"'
new_lst1 = []
finally_str = ''
for data in lst1:
    if data.isdigit() == True or data.startswith("+") or data.startswith("-"):
        if len(data) == 1:
            data_replace = data.replace(data, "0" + data)
            new_lst1.append(data_replace)
            index_data = new_lst1.index(data_replace)
            new_lst1.insert(index_data, quotation_mark)
            index_data += 2
            new_lst1.insert(index_data, quotation_mark)
        elif data.startswith("+"):
            if len(data) == 2:
                data_replace = data.replace("+", "+0")
                new_lst1.append(data_replace)
                index_data = new_lst1.index(data_replace)
                new_lst1.insert(index_data, quotation_mark)
                index_data += 2
                new_lst1.insert(index_data, quotation_mark)
            else:
                new_lst1.append(data)
                index_data = new_lst1.index(data)
                new_lst1.insert(index_data, quotation_mark)
                index_data += 2
                new_lst1.insert(index_data, quotation_mark)
        elif data.startswith("-"):
            if len(data) == 2:
                data_replace = data.replace("-", "-0")
                new_lst1.append(data_replace)
                index_data = new_lst1.index(data_replace)
                new_lst1.insert(index_data, quotation_mark)
                index_data += 2
                new_lst1.insert(index_data, quotation_mark)
            else:
                new_lst1.append(data)
                index_data = new_lst1.index(data)
                new_lst1.insert(index_data, quotation_mark)
                index_data += 2
                new_lst1.insert(index_data, quotation_mark)
        else:
            new_lst1.append(data)
            index_data = new_lst1.index(data)
            new_lst1.insert(index_data, quotation_mark)
            index_data += 2
            new_lst1.insert(index_data, quotation_mark)
    else:
        new_lst1.append(data)


print("Исходный список: ",lst1)
print("Новый список: ",new_lst1)


for index,element in enumerate(new_lst1):
    index_next = index + 1
    if element == '"':
        if index_next == len(new_lst1):
            finally_str += element + ''
        elif new_lst1[index_next].isdigit() == True or new_lst1[index_next].startswith("+") or new_lst1[index_next].startswith("-"):
            finally_str += element + ''
        else:
            finally_str += element + ' '
    elif element.isdigit() == True or element.startswith("+") or element.startswith("-"):
        finally_str += element + ''
    else:
        finally_str += element + ' '

# for index,element in enumerate(new_lst1):
#     index_next = index + 1
#     if element == '"' and (new_lst1[index_next].isdigit() == True or new_lst1[index_next].startswith("+") or new_lst1[index_next].startswith("-")):
#         finally_str += element + ''
#     elif element.isdigit() == True or element.startswith("+") or element.startswith("-"):
#         finally_str += element + ''
#     else:
#         finally_str += element + ' '


print("Окончательная строка: ",finally_str)






