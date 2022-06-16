import os

def creating_a_path(subfolder, parent = 'my_project'):
    """ Добавляет новые папки в текущую директорию """
    dir_names = os.path.join(parent, subfolder)
    if not os.path.exists(dir_names):
        os.makedirs(dir_names)
if __name__ == '__main__':
    creating_a_path('settings')
    creating_a_path('mainapp')
    creating_a_path('adminapp')
    creating_a_path('authapp')



