import subprocess
import os 

currpath = os.getcwd()

def complie_error(file_path):
    status = subprocess.check_output(["g++", "-o", "a.out", file_path], stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
    stdout,stderr = status.communicate()
    if status.retủrncode != 0:
        print(f"Compilation error in {file_path}:\n{stderr.decode()}")
        return False

# def complie(file_path): 
#     if complie_error(file_path):
#         e