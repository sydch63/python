import requests
import sys

url = 'http://www.cbr.ru/scripts/XML_daily.asp'

def currency_rates(url,val):
    response = requests.get(url)
    encodings = requests.utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    content_split = content.split("Valute ID")
    dct_valute = {}
    for index,value in enumerate(content_split):
        value = value.split("/")
        for idx,valute in enumerate(value):
            if idx == 1:
                valute_name = valute.split('>')[2].replace("<",'')
                dct_valute.setdefault(valute_name)
            elif idx == 4:
                valute_price = valute.split('>')[2].replace("<",'').replace(",",".")
                dct_valute[valute_name] = float(valute_price)
    return dct_valute.get(val.upper())




if len(sys.argv) == 1:
    print("Введите валюту")
elif len(sys.argv) > 2:
    print("Введите только одну валюту")
elif currency_rates(url,sys.argv[1]) is None:
    print(f'{sys.argv[1]} : Не найдена валюта')
else:
    print(currency_rates(url, sys.argv[1]))