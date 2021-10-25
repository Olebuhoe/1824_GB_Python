"""
Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница
размера файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках), размер которых
не превышает этой границы, но больше предыдущей (начинаем с 0), например:
    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }
Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
"""
import os


def count_files_by_size(folder):
    gloss = {}
    names = os.listdir(folder)
    paths = [os.path.join(folder, name) for name in names]
    sizes = [(os.stat(path).st_size) for path in paths]
    sizes_sort = sorted(sizes)
    size_borders = [10 ** i for i in range(len(str((sizes_sort)[-1])) + 1)]
    for i in range(len(size_borders) - 1):
        gloss[size_borders[i + 1]] = len([item.name for item in os.scandir(folder)
                                          if size_borders[i] < item.stat().st_size < size_borders[i + 1]])
    return gloss


# print(count_files_by_size('some_files'))
