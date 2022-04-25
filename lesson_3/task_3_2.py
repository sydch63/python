dct_eng_rus = {"one":"один","two":"два","three":"три","four":"четыре","five":"пять","six":"шесть","seven":"семь","eight":"восемь","nine":"девять","ten":"десять"}

def num_translate_adv(word):
    if word.istitle() is True:
        word = word.lower()
        return dct_eng_rus.get(word).capitalize()
    else:
        word = word.lower()
        return dct_eng_rus.get(word)


num_translate_adv("One")
num_translate_adv("5")
num_translate_adv("eleven")
num_translate_adv("Five")
num_translate_adv("six")

#не очень понял из ТЗ, как требуется показать None, имелось ввиду показать что функция не может перевести и показать type = None?
#или достаточно , что она вернет None "скрытно" как у меня сейчас