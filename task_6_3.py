import sys
from itertools import zip_longest

txt1 = [
    'Иванов,Иван,Иванович\n',
    'Петров,Петр,Петрович\n',
    'Тихонов,Тихон,Тихонович\n',
    'Сидоров,Сидор,Сидорович\n'
]
txt2 = [
    'скалолазание,охота\n',
    'ходьба на месте,рыбалка\n',
    'горные лыжи\n'
]

with open('person.csv', 'w', encoding='utf-8') as f_1:
    f_1.writelines(txt1)
with open('hobby.csv', 'w', encoding='utf-8') as f_2:
    f_2.writelines(txt2)
with open('person.csv', 'r', encoding='utf-8') as f_1:
    _person = f_1.readlines()
    person = [*map(lambda x: x[:-1], _person)]
with open('hobby.csv', 'r', encoding='utf-8') as f_2:
    _hobby = f_2.readlines()
    hobby = [*map(lambda x: x[:-1], _hobby)]
# print(person)
# print(type(person))
# print(hobby)
if len(person) >= len(hobby):
    gloss = {key: value for key, value in zip_longest(person, hobby)}
else:
    sys.exit(1)
print(gloss)
with open('info.csv', 'w', encoding='utf-8') as f:
    for key, value in gloss.items():
        f.write(f'{key}: {value}\n')
