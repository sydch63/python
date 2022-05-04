import utils

url = 'http://www.cbr.ru/scripts/XML_daily.asp'

print(utils.currency_rates_advanced(url,'UsD'))
print(utils.currency_rates_advanced(url, "EuR"))
print(utils.currency_rates_advanced(url, "GBP"))
print(utils.currency_rates_advanced(url, "GBP2"))

print(utils.currency_rates(url,'UsD'))
print(utils.currency_rates(url,"EuR"))
print(utils.currency_rates(url,'GBP2'))
print(utils.currency_rates(url,'GBP'))