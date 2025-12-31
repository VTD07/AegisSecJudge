import os 

def abs_path(current_path,relative_path):
    return os.path.join(current_path, relative_path)

def check_file_1(relative_path): #check file support
    return os.path.exists(relative_path)

def check_folder_2(currpath, relative_path): #check folder support
    full_path = abs_path(currpath, relative_path)
    return os.path.exists(full_path)