import subprocess
import sys
import os 


currpath = os.getcwd()
test_folder = os.path.join(currpath, "test_folder\\TONGCSNMOD")


def complie_error(file_path):
    status = subprocess.run([sys.executable, "-m", "py_compile", file_path], cwd=currpath, capture_output=True, text=True)
    return status.returncode != 0

def detect_RTE_TLE_AC(file_path):
    try:
        
        for i in range(1,21):
            
            index=f"{i:02d}"
            
            input_folder_path = os.path.join(test_folder,f"Test{index}")
            input_file_path=os.path.join(input_folder_path,f"TONGCSNMOD.inp")
            output_file_path=os.path.join(input_folder_path,f"TONGCSNMOD.out")
            
            with open(input_file_path, 'r') as input_file, open(output_file_path, 'r') as output_file:
                status = subprocess.run([sys.executable,file_path], input=input_file.read(), capture_output=True, text=True, timeout=1)
                if status.returncode != 0:
                    print(f"RTE on test case {index}")
                    return "RTE"
                else: 
                    if status.stdout.strip() != output_file.read().strip():
                        print(f"WA on test case {index}")
                        return "WA"

    except subprocess.TimeoutExpired:
        print(f"TLE on test case {index}")
        return "TLE"
    
    return "AC"
    
def complie(file_path): 
    if complie_error(file_path):
        print(f"Error: Compilation failed for {file_path}")
    else: 
        result = detect_RTE_TLE_AC(file_path)
        print(f"Program resulted in: {result}")