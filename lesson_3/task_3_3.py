def thesaurus(*names):
    dct_name = {}
    sort_dct_name = {}
    for name in names:
        word = name[0]
        if dct_name.setdefault(word) is not None:
            dct_name[word].append(name)
        else:
            dct_name[word] = []
            dct_name[word].append(name)
    for key in sorted(dct_name.keys()):
        sort_dct_name[key] = dct_name[key]
    return print(sort_dct_name)

thesaurus("Иван", "Мария", "Петр", "Илья", "Артем", "Вадим", "Анатолий","Павел","Яков","Федор","Кирилл","Макс","Евгений")