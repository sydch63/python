import requests

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

print(currency_rates(url,'UsD'))
print(currency_rates(url,'rUB'))
print(currency_rates(url,'KZT'))