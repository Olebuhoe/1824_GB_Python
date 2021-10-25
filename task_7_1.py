"""
Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp
Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как лучше хранить конфигурацию
этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект; можно ли будет при этом расширять
конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
"""
import os


def struct_project(folder, root_dir, *dir_names):
    if os.path.exists(os.path.join(folder, root_dir)):
        print('Выберите другое имя для корневой папки проекта или измените имя уже существующей папки')
    else:
        for i in range(len(dir_names)):
            os.makedirs(os.path.join(folder, root_dir, [*dir_names][i]), exist_ok=True)


# struct_project(r'D:\PycharmProjects\GB\lesson_7', 'my_proj', 'settings', 'mainapp', 'adminapp', 'authapp')
arr = ['settings', 'mainapp', 'adminapp', 'authapp']
struct_project(r'D:\PycharmProjects\GB\lesson_7', 'my_proj', *arr)

