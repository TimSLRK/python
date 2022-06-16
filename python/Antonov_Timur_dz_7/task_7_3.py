import shutil

def func(name):
    """ Копирует необходимые данные в новую директорию, которая указана в пути """
    shutil.copytree(f"my_project_1/{name}/templates", f'my_project_1/templates', dirs_exist_ok=True)
func('authapp')
func('mainapp')


