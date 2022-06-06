import requests
import json

URL = 'https://www.cbr-xml-daily.ru/daily_json.js'


def currency_rates(cur_code):
    """
    Displays the exchange rate in rubles
    :param cur_code: currency code
    :return: value in rubles
    """
    response = requests.get(URL)
    rate = json.loads(response.text)
    cur_code = cur_code.upper()
    quit_data = ''
    for key in rate["Valute"]:
        if cur_code == key:
            result = rate["Valute"][cur_code]["Value"]
            quit_data = f'Курс {cur_code} = {result} руб'
            break
        else:
            quit_data = None
    return quit_data

if __name__ == '__main__':
    print(currency_rates('USD'))
    print(currency_rates('EUR'))
    print(currency_rates('ABC'))
