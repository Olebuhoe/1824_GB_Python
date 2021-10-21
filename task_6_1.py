with open('nginx_logs.txt', encoding='utf-8') as file:
    for line in file:
        _data = tuple(f'{line.split()[0]}, {line.split()[5][1:]}, {line.split()[6]}'.split(','))
        print(_data)

