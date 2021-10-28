import re
from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        for arg in args:
            print(f'{func.__name__}({arg}: {type(arg)})', end=', ')
        for k, v in kwargs.items():
            print(f'{func.__name__}({v}: {type(v)})')
        # print() # можно добавить, тогда результат оборачиваемой функции будет выходить на новой строке
        return result

    return wrapper


@type_logger
def kek(x, y, z):
    return int(x * y) * z


print(kek(4, 2.5, z='cat'))


@type_logger
def email_parse(e_mail):
    if re.findall(r'^([a-zA-Z0-9_.+-]+)@([a-zA-Z0-9-]+(?:\.[a-zA-Z0-9]+)+)$', e_mail):
        return dict(zip(('username', 'domain'),
                        *re.findall(r'^([a-zA-Z0-9_.+-]+)@([a-zA-Z0-9-]+(?:\.[a-zA-Z0-9]+)+)$', e_mail)))
    else:
        raise ValueError(f'wrong e-mail: {e_mail}')


print(email_parse('dr.junk@mail.ru'))


@type_logger
def thesaurus(*args):
    # для формирования ключей словаря вытаскиваем первые буквы имен, оставляем уникальные
    array_for_key = []
    for i in args:
        array_for_key.append(i[0])
    letter_for_key = list(set(array_for_key))
    # собираем в словарь пары ключ-значение для соответствующих букв-слов
    gloss_new = {}
    for i in args:
        for j in letter_for_key:
            if i[0] == j:
                gloss_new[j] = i
    # меняем тип значений словаря на список и добавляем из начальных имен те, которые не вошли
    gloss_new = {k: [v] for k, v in gloss_new.items()}
    for k in gloss_new:
        for i in args:
            if i[0] == k and i not in gloss_new[k]:
                gloss_new[k].append(i)
    gloss_fin = sorted(gloss_new.items())  # сортируем
    return gloss_fin


print(thesaurus('Иван', 'Григорий', 'Илья', 'Николай', 'Нина', 'Михаил', 'Игорь'))
