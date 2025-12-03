import subprocess
import os 

currpath = os.getcwd()
file_path = os.path.join(currpath, "pending\\C++\\Test.cpp")
exe_path = os.path.join(currpath, "pending\\C++\\Test.exe")
test_folder = os.path.join(currpath, "test_folder\\Accepted")

def complie_error(file_path):
    status = subprocess.run(["g++", file_path, "-o"], cwd=currpath, capture_output=True, text=True)
    return status.returncode != 0

def detect_RTE_TLE(filepath): 
    try:
        with open(test_folder, "r") as f:
            process = subprocess.run(
                [exe_path],              
                stdin=f,
                capture_output=True,
                text=True,
                timeout=1                
            )

        if process.returncode != 0:
            return "RTE"

        return "OK"

    except subprocess.TimeoutExpired:
        return "TLE"
    
def complie(file_path): 
    if not complie_error(file_path):
        print(f"Error: Compilation failed for {file_path}")
        # os.rename(os.path.join(currpath, file_path), os.path.join(currpath, "processed\\CE\\C++", os.path.basename(file_path))) #move to CE folder
    else: 
        print("Compiled Successfully")
        print(detect_RTE_TLE(exe_path))