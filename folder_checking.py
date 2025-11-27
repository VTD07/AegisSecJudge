import os 

def abs_path(current_path,relative_path):
    return os.path.join(current_path, relative_path)

def check_folder_1(relative_path):
    if not os.path.exists(relative_path): 
        print(f"Error: doesn't have {relative_path} folder to process")
        return False

def check_folder_2(currpath, relative_path):
    full_path = abs_path(currpath, relative_path)
    if not os.path.exists(full_path): 
        print(f"Error: doesn't have {relative_path} folder to process")
        return False
    return True
    