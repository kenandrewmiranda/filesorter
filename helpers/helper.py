import os
import shutil

'''
These functions are responsible for supporting the logic of the application.
'''

def get_file_list(folder_path):
    return os.listdir(folder_path)

def get_extension_list(file_list, folder_path):
    return {file.split(".")[-1] for file in file_list if os.path.isfile(os.path.join(folder_path, file))}

def is_actual_file(file, folder_path):
    return os.path.isfile(os.path.join(folder_path, file))

def create_folders(extensions, folder_path):
    for ext in extensions:
        folder_path_for_ext = os.path.join(folder_path, ext)
        if not os.path.exists(folder_path_for_ext) and ext != 'ini':
            os.makedirs(folder_path_for_ext)

def move_file(file, folder_path):
    file_path = os.path.join(folder_path, file)
    if is_actual_file(file, folder_path):
        file_extension = file.split(".")[-1]
        if file != file_extension:
            new_path = os.path.join(folder_path, file_extension, file)
            shutil.move(file_path, new_path)