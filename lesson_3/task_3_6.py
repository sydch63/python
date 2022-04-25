# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх заданных списков.
# Условие задачи
import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(number_of_jokes,nouns,adverbs,adjectives,uniq=False):
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


get_jokes(3,nouns,adverbs,adjectives,uniq=True)