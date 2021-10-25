"""
Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике). Написать
скрипт, который собирает все шаблоны в одну папку templates, например:
|--my_project
   ...
  |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
(они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача, которая
решена, например, во фреймворке django.
"""
import os
import shutil


def copy_tree(dst, *src, symlinks=False, ignore=None):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for i in range(len(src)):
        for item in os.listdir([*src][i]):
            source = os.path.join([*src][i], item)
            dest = os.path.join(dst, item)
            if os.path.isdir(source):
                shutil.copytree(source, dest, symlinks, ignore)
            else:
                shutil.copy2(source, dest)


arr = [r'D:\PycharmProjects\GB\lesson_7\my_project\authapp\templates',
       r'D:\PycharmProjects\GB\lesson_7\my_project\mainapp\templates']
copy_tree(r'D:\PycharmProjects\GB\lesson_7\my_project\templates', *arr)
# или так:
# copy_tree(r'D:\PycharmProjects\GB\lesson_7\my_project\templates',
#           r'D:\PycharmProjects\GB\lesson_7\my_project\authapp\templates',
#           r'D:\PycharmProjects\GB\lesson_7\my_project\mainapp\templates')
