"""
Есть два списка:
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
('Иван', '9А')
('Анастасия', '7В')
...
Количество генерируемых кортежей не должно быть больше длины списка tutors. Если в списке klasses меньше элементов, чем
в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None), например:
('Станислав', None)

### Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения. Подумать, в каких ситуациях
генератор даст эффект.

"""
from itertools import zip_longest

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Станислав'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б'
]


def gen_tpl(name_lst, klass_lst):
    if len(name_lst) >= len(klass_lst):
        for _ in zip_longest(name_lst, klass_lst):
            yield _
    elif len(name_lst) < len(klass_lst):
        for _ in zip(name_lst, klass_lst):
            yield _


tpl = gen_tpl(tutors, klasses)
print(next(tpl))
print(next(tpl))
print(next(tpl))
print(next(tpl))
print(next(tpl))
print(next(tpl))
print(next(tpl))
print(next(tpl))
print(next(tpl))
print(next(tpl))
