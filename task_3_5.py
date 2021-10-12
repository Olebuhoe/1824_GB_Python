"""
Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков
(по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
        	Например:
>>> get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]

Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках (когда каждое слово
можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
"""
import random as rd

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count: int, rep: bool = True):
    """
     Генерирует шутки, сформированные из трех случайных слов, взятых из трёх списков (по одному из каждого): nouns,
     adverbs, adjective.
    :param count: количество шуток, которые нужно получить.
    :param rep: False - запрещает повторы любых слов в шутках, True(по умолчанию) - разрешает.
    :return: список с указанным количеством шуток.
    """
    lst = [nouns, adverbs, adjectives]
    humor = []
    if rep is True:
        if count <= 5:
            for j in lst:
                rd.shuffle(j)
            for name, login, role in zip(nouns[:count], adverbs, adjectives):
                humor.append(f'{name}, {login}, {role}')
            return humor
        else:
            for i in range(count // 5 + 1):
                for j in lst:
                    rd.shuffle(j)
                for name, login, role in zip(nouns, adverbs, adjectives):
                    humor.append(f'{name}, {login}, {role}')
            return humor[:count]
    else:
        if count <= 5:
            for j in lst:
                rd.shuffle(j)
            for name, login, role in zip(nouns[:count], adverbs, adjectives):
                humor.append(f'{name}, {login}, {role}')
            return humor
        else:
            return 'Выставленное значение аргумента "rep" запрещает повторы слов в шутках. Уменьшите параметр ' \
                   'количества шуток, либо разрешите повторы слов.'


print(get_jokes(11, rep=True))
