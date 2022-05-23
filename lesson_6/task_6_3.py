import json

dct_result = {}
file_users = open('task_3_users.csv','r',encoding='utf-8')
file_hobby = open('task_3_hobby.csv','r',encoding='utf-8')
file_result = open('task_3_rezult.txt','w',encoding='utf-8')

lst_user = file_users.read().split('\n')
lst_hobby = file_hobby.read().split('\n')
file_users.close()
file_hobby.close()

if len(lst_user) < len(lst_hobby):
    for val, el in enumerate(lst_user):
        if val + 1 < len(lst_user):
            dct_result[el.split(',')[0][0] + el.split(',')[1][0] + el.split(',')[2][0]] = lst_hobby[val].replace(',', ';')
        else:
            dct_result[el.split(',')[0][0] + el.split(',')[1][0] + el.split(',')[2][0]] = lst_hobby[val].replace(',',';')
            file_result.write(json.dumps(str(dct_result),ensure_ascii=False))
            file_result.close()
            exit('Количество хобби больше')
elif len(lst_user) == len(lst_hobby):
    for val, el in enumerate(lst_user):
        dct_result[el.split(',')[0][0] + el.split(',')[1][0] + el.split(',')[2][0]] = lst_hobby[val].replace(',', ';')
    file_result.write(json.dumps(str(dct_result),ensure_ascii=False))
    file_result.close()
else:
    for val, el in enumerate(lst_user):
        if val < len(lst_hobby):
            dct_result[el.split(',')[0][0] + el.split(',')[1][0] + el.split(',')[2][0]] = lst_hobby[val].replace(',', ';')
        else:
            dct_result[el.split(',')[0][0] + el.split(',')[1][0] + el.split(',')[2][0]] = None
    file_result.write(json.dumps(str(dct_result),ensure_ascii=False))
    file_result.close()