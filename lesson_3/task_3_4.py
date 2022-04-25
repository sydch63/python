def thesaurus_adv(*names):
    dct_surname = {}
    sort_dct_name = {}
    dct_new = {}
    dct_name = {}
    for name in names:
        name_split = name.split(" ")
        word_surname = name_split[1][0]
        word_name = name_split[0][0]
        name = name_split[1] + ' ' + name_split[0] #Усложнение
        if word_name not in dct_new.keys():
            dct_new[word_name] = []
            dct_name[word_name] = []
            dct_name[word_name].append(name)
            if word_surname not in dct_surname.keys():
                dct_surname[word_surname] = dct_name.copy()
                dct_name.clear()
            else:
                dct_surname[word_surname][word_name] = []
                dct_surname[word_surname][word_name].append(name)
                dct_name.clear()
        else:
            if word_surname not in dct_surname.keys():
                dct_name[word_name] = []
                dct_name[word_name].append(name)
                dct_surname[word_surname] = dct_name.copy()
                dct_name.clear()
            else:
                dct_surname[word_surname][word_name].append(name)
    for key_surname in sorted(dct_surname.keys()):
        for key_name in sorted(dct_surname[key_surname].keys()):
            if key_surname in sort_dct_name.keys():
                sort_dct_name[key_surname][key_name] = dct_surname[key_surname][key_name]
            else:
                sort_dct_name[key_surname] = {}
                sort_dct_name[key_surname][key_name] = dct_surname[key_surname][key_name]
    return sort_dct_name

thesaurus_adv("Иван Сергеев", "Алла Сидорова", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Василий Суриков")