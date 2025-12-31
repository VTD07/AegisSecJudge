import pre_check.folder_checking as fc 
import subprocess 
import os 

currpath = os.getcwd()

ness_folder = [
    "complier"
    "test_folder", 
    "pending", 
    "db"
]

def check_folder(): 
    for i in ness_folder: 
        
        path = os.path.join(currpath,i)
        if not fc.check_file_1(path): 
            return False, i
    
    return True, "NONE" 

def check_complier(): 
    cmd = (["g++","--version"],["gcc","--version"],["python","--version"])
    for i in cmd:
        try: subprocess.run(i,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
        except FileNotFoundError: 
            return False, i[0]

    return True, "NONE" 

value_1, folder = check_folder()
value_2, compiler = check_complier()

if value_2 == False: 
    print(f"check for {compiler}")
    
elif value_2 == False: 
    print(f"check for f{folder}")
    
else: 
    print("All clear")