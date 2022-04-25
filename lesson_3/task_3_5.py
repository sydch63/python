import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(number_of_jokes,nouns=nouns,adverbs=adverbs,adjectives=adjectives):
    jokes = []
    '''Цикл , с помощью random.choice, выбираем рандомные слова из заданных списков и добавляеем их в конечный список'''
    while number_of_jokes != 0:
        word_nouns = random.choice(nouns)
        word_adverbs = random.choice(adverbs)
        word_adjectives = random.choice(adjectives)
        jokes_str = f"{word_nouns} {word_adverbs} {word_adjectives}"
        jokes.append(jokes_str)
        number_of_jokes -= 1
    return jokes

get_jokes(10,nouns,adverbs,adjectives)