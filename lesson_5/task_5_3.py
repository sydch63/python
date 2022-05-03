tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
groups = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

def students_and_classes(tutors,groups):
    for idx,stud in enumerate(tutors):
        if idx == len(tutors):
            return stud(groups[idx])
        elif len(groups) > idx:
            yield stud,groups[idx]
        else:
            yield stud,None




gen_fin = students_and_classes(tutors,groups)

print(f'Результат, где учеников меньше')
print(f'Ученики: {tutors}')
print(f'Классы: {groups}')
print(f'Тип объекта: {type(gen_fin)}')
print("Все значения генератора: ")
for i in gen_fin:
    print(i)

print("\n")

print(f'Результат, где учеников больше')
groups = [
    '9А', '7В', '9Б', '9В'
]
gen_fin = students_and_classes(tutors,groups)
print(f'Ученики: {tutors}')
print(f'Классы: {groups}')
print(f'Тип объекта: {type(gen_fin)}')
print("Все значения генератора: ")
for i in gen_fin:
    print(i)