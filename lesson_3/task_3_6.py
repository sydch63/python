import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(number_of_jokes,nouns=nouns,adverbs=adverbs,adjectives=adjectives,uniq=False):
    jokes = []
    '''Проверяем на количество шуток вкупе с уникальностью, с помощью random.sample создаем только уникальные списки из изначальных'''
    if number_of_jokes > 5 and uniq == True:
        print ("Количество уникальных шуток, может быть только 5")
        number_of_jokes = 5
        lst_nouns = random.sample(nouns, number_of_jokes)
        lst_adverbs = random.sample(adverbs, number_of_jokes)
        lst_adjectives = random.sample(adjectives, number_of_jokes)
    elif number_of_jokes <= 5 and uniq == True:
        lst_nouns = random.sample(nouns, number_of_jokes)
        lst_adverbs = random.sample(adverbs, number_of_jokes)
        lst_adjectives = random.sample(adjectives, number_of_jokes)
    '''Цикл , где If это уникальные список шуток , а все остальное - любая шутка'''
    while number_of_jokes != 0:
        if uniq == True:
            word_nouns = random.choice(lst_nouns)
            lst_nouns.remove(word_nouns)
            word_adverbs = random.choice(lst_adverbs)
            lst_adverbs.remove(word_adverbs)
            word_adjectives = random.choice(lst_adjectives)
            lst_adjectives.remove(word_adjectives)
            jokes_str = f"{word_nouns} {word_adverbs} {word_adjectives}"
            jokes.append(jokes_str)
            number_of_jokes -= 1
        else:
            word_nouns = random.choice(nouns)
            word_adverbs = random.choice(adverbs)
            word_adjectives = random.choice(adjectives)
            jokes_str = f"{word_nouns} {word_adverbs} {word_adjectives}"
            jokes.append(jokes_str)
            number_of_jokes -= 1
    return jokes



get_jokes(7,nouns,adverbs,adjectives)

#Опять не понял по ТЗ, мы должны в этом задании выводить максимум 5(столько может быть уникальных шуток) или
#выводить 5 плюс столько сколько задал пользователь, но у же не уникальных
#Ниже функция, которая сделает 5 уникальных + столько сколько задали , но не уникальных
# def get_jokes(number_of_jokes,*args,uniq=False):
#     jokes = []
#     '''Проверяем на количество шуток вкупе с уникальностью, с помощью random.sample создаем только уникальные списки из изначальных'''
#     number_of_jokes_no_uniq = number_of_jokes
#     number_of_jokes = 5
#     if number_of_jokes > 5 and uniq is True:
#         print ("Количество уникальных шуток, может быть только 5")
#         lst_nouns = random.sample(nouns, number_of_jokes)
#         lst_adverbs = random.sample(adverbs, number_of_jokes)
#         lst_adjectives = random.sample(adjectives, number_of_jokes)
#     elif number_of_jokes <= 5 and uniq is True:
#         lst_nouns = random.sample(nouns, number_of_jokes)
#         lst_adverbs = random.sample(adverbs, number_of_jokes)
#         lst_adjectives = random.sample(adjectives, number_of_jokes)
#     '''Цикл , где If это уникальные список шуток , а все остальное - любая шутка'''
#     while number_of_jokes_no_uniq != 0:
#         if uniq is True and number_of_jokes != 0 :
#             while number_of_jokes != 0:
#                 word_nouns = random.choice(lst_nouns)
#                 lst_nouns.remove(word_nouns)
#                 word_adverbs = random.choice(lst_adverbs)
#                 lst_adverbs.remove(word_adverbs)
#                 word_adjectives = random.choice(lst_adjectives)
#                 lst_adjectives.remove(word_adjectives)
#                 jokes_str = f"{word_nouns} {word_adverbs} {word_adjectives}"
#                 jokes.append(jokes_str)
#                 number_of_jokes -= 1
#                 number_of_jokes_no_uniq -= 1
#         else:
#             word_nouns = random.choice(nouns)
#             word_adverbs = random.choice(adverbs)
#             word_adjectives = random.choice(adjectives)
#             jokes_str = f"{word_nouns} {word_adverbs} {word_adjectives}"
#             jokes.append(jokes_str)
#             number_of_jokes_no_uniq -= 1
#     return jokes