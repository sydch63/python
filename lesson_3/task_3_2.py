dct_eng_rus = {"one":"один","two":"два","three":"три","four":"четыре","five":"пять","six":"шесть","seven":"семь","eight":"восемь","nine":"девять","ten":"десять"}

def num_translate_adv(word):
    if word.istitle() is True:
        word = word.lower()
        return print(dct_eng_rus.get(word).capitalize())
    else:
        word = word.lower()
        return print(dct_eng_rus.get(word))


num_translate_adv("One")
num_translate_adv("5")
num_translate_adv("eleven")
num_translate_adv("Five")
num_translate_adv("six")