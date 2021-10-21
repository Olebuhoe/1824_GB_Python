from collections import Counter


def max_count_elem(lst, how):  # функция не универсальная, подойдет только для конкретного списка
    """Функция для определения количества наиболее часто встречающихся элементов в списке"""
    ip_list = []
    for i in lst:
        ip_list.append(i[0])
    return Counter(ip_list).most_common(how)


with open('nginx_logs.txt', encoding='utf-8') as file:
    log_list = []
    for line in file:
        _data = tuple([f'{line.split()[0]}, {line.split()[5][1:]}, {line.split()[6]}'.split(',')])
        log_list.extend(_data)
# print(log_list)
print(f'С данного IP-адреса: {max_count_elem(log_list, 1)[0][0]}, было отправлено максимальное количество запросов, '
      f'а именно: {max_count_elem(log_list, 1)[0][1]}.')
print(max_count_elem(log_list, 3))  # для примера, следующие по частоте запросов айпишники
