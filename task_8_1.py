import re


def email_parse(e_mail):
    if re.findall(r'^([A-Za-z0-9._%+-]+)@([A-Za-z0-9.-]+\.[A-Za-z]+)$', e_mail):
        return dict(zip(('username', 'domain'),
                        *re.findall(r'^([A-Za-z0-9._%+-]+)@([A-Za-z0-9.-]+\.[A-Za-z]+)$', e_mail)))
    else:
        raise ValueError(f'wrong e-mail: {e_mail}')


print(email_parse('kot-kokos@mail.ru'))
# print(email_parse('dfghmndghm'))
