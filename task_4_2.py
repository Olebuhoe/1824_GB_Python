from cbr_parser.utils import extract_data


def currency_rates(currency_code: str):
    """
    Возвращает текущий курс выбранной валюты по отношению к рублю
    :param currency_code: код валюты (например, USD, EUR, GBP, ...)
    :return: количество рублей за единицу выбранной валюты
    """
    # currency_code = input('Введите код валюты в формате USD, EUR, GBP и т.п.: ').upper()
    # можно запросить аргумент, тогда не указываем его в функции: currency_rates()
    gloss = {key: value for key, value in zip(extract_data('CharCode'), extract_data('Value'))}
    for key in gloss:
        if currency_code.upper() == key:
            return float(format(float(gloss[key].replace(',', '.')), '.2f'))


rub_per_cur = currency_rates('USD')
print(rub_per_cur)
print(type(rub_per_cur))
rub_per_cur = currency_rates('eur')
print(rub_per_cur)
