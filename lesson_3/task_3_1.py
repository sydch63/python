dct_eng_rus = {"one":"один","two":"два","three":"три","four":"четыре","five":"пять","six":"шесть","seven":"семь","eight":"восемь","nine":"девять","ten":"десять"}

def num_translate(word):
    word = word.lower()
    return print(dct_eng_rus.get(word))


num_translate("one")
num_translate("5")
num_translate("eleven")
num_translate("Five")