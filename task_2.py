from requests import get, utils

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)

list_all = (content.split('</NumCode><CharCode>')[1:])  # список со строками, где в одной строке, и имя, и значениеprint(content)

dict_correlation = {}
for i in range(len(list_all)):
    list_first = (content.split('</NumCode><CharCode>')[1:][i].split('</Name><Value>'))  # список, где начало в первом имя, во втором цена
    list_name = (content.split('</NumCode><CharCode>')[1:][i].split('</Name><Value>')[0].split('</CharCode><Nominal>')[0])  # имя
    list_price = (content.split('</NumCode><CharCode>')[1:][i].split('</Name><Value>')[1].split('</Value></Valute>')[0])  # цена
    dict_correlation[list_name] = list_price


def currency_rates(name):
    try:
        print(f'{name.lower().upper()} = {dict_correlation[name.lower().upper()]}')
    except:
        print(f'{name.lower().upper()} = {None}')

currency_rates('euR')
currency_rates('usd')
currency_rates('sadadasd')
currency_rates(input('Введите валюту: '))