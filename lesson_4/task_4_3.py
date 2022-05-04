import requests
import datetime

url = 'http://www.cbr.ru/scripts/XML_daily.asp'

def currency_rates_advanced(url,val):
    response = requests.get(url)
    encodings = requests.utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    content_split = content.split("Valute ID")
    date_lst = content_split[0].split()[3].split('"')[1].split('.')
    date = datetime.date(int(date_lst[2]), int(date_lst[1]), int(date_lst[0]))
    dct_valute = {}
    lst_valute = []
    for index,value in enumerate(content_split):
        value = value.split("/")
        for idx,valute in enumerate(value):
            if idx == 1:
                valute_name = valute.split('>')[2].replace("<",'')
                dct_valute.setdefault(valute_name)
            elif idx == 4:
                valute_price = valute.split('>')[2].replace("<",'').replace(",",".")
                dct_valute[valute_name] = float(valute_price)
    lst_valute.append(date)
    lst_valute.append(dct_valute.get(val.upper()))
    return lst_valute

print(currency_rates_advanced(url,'UsD'))
print(currency_rates_advanced(url, "EuR"))
print(currency_rates_advanced(url, "GBP"))
print(currency_rates_advanced(url, "GBP2"))