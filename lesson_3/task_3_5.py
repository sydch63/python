# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх заданных списков.
# Условие задачи
import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(number_of_jokes,nouns,adverbs,adjectives):
    jokes = []
    while number_of_jokes != 0:
        word_nouns = random.choice(nouns)
        word_adverbs = random.choice(adverbs)
        word_adjectives = random.choice(adjectives)
        jokes_str = word_nouns+ ' ' +word_adverbs+ ' ' +word_adjectives
        jokes.append(jokes_str)
        number_of_jokes -= 1
    return jokes

get_jokes(3,nouns,adverbs,adjectives)