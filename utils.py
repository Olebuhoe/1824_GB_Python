from cbr_parser.utils import extract_data


def currency_rates(currency_code: str):
    """
    Возвращает текущий курс выбранной валюты по отношению к рублю
    :param currency_code: код валюты (например, USD, EUR, GBP, ...)
    :return: количество рублей за единицу выбранной валюты
    """
    gloss = {key: value for key, value in zip(extract_data('CharCode'), extract_data('Value'))}
    for key in gloss:
        if currency_code.upper() == key:
            return float(format(float(gloss[key].replace(',', '.')), '.2f'))


if __name__ == '__main__':
    # пример использования
    rub_per_cur = currency_rates('USD')
    print(rub_per_cur)
