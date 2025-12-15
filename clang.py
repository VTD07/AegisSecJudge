import subprocess
import os 

currpath = os.getcwd()
file_path = os.path.join(currpath, "pending\\C++\\Test.cpp")
exe_path = os.path.join(currpath, "pending\\C++\\Test.exe")
test_folder = os.path.join(currpath, "test_folder\\Accepted\\TONGCSNMOD")


def complie_error(file_path):
    status = subprocess.run(["g++", file_path, "-o"], cwd=currpath, capture_output=True, text=True)
    return status.returncode != 0

def detect_RTE_TLE_AC(file_path):
    try:
        
        for i in range(1,21):
            
            if(i<10):k=f"0{i}"
            else :k=f"{i}"
            
            input_folder_path = os.path.join(test_folder,f"Test{k}")
            input_file_path=os.path.join(input_folder_path,f"TONGCSNMOD.inp")
            output_file_path=os.path.join(input_folder_path,f"TONGCSNMOD.out")
            
            with open(input_file_path, 'r') as input_file, open(output_file_path, 'r') as output_file:
                status = subprocess.run([file_path], input=input_file.read(), capture_output=True, text=True, timeout=1)
                if status.returncode != 0:
                    print(f"RTE on test case {k}")
                    return "RTE"
                else: 
                    if status.stdout.strip() != output_file.read().strip():
                        print(f"WA on test case {k}")
                        return "WA"

    except subprocess.TimeoutExpired:
        print(f"TLE on test case {k}")
        return "TLE"
    
    return "AC"
    
def complie(file_path): 
    if not complie_error(file_path):
        print(f"Error: Compilation failed for {file_path}")
    else: 
        result = detect_RTE_TLE_AC(exe_path)
        if result:
            print(f"Program resulted in: {result}")
        else:
            print("Program executed successfully without RTE or TLE.")