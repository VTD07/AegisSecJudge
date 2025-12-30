import subprocess
import sys
import os 


currpath = os.getcwd()
# test_folder = os.path.join(currpath, "test_folder\\TONGCSNMOD")


def complie_error(file_path):
    status = subprocess.run([sys.executable, "-m", "py_compile", file_path], cwd=currpath, capture_output=True, text=True)
    return status.returncode != 0

def detect_RTE_TLE_AC(file_path, test_folder, test_id, time_limit):
    try:

        for i in range(1,len(os.listdir(test_folder))+1):        
            
            index=f"{i:02d}"
            
            input_folder_path = os.path.join(test_folder,f"Test{index}")
            input_file_path=os.path.join(input_folder_path,f"{test_id}.inp")
            output_file_path=os.path.join(input_folder_path,f"{test_id}.out")
            
            with open(input_file_path, 'r') as input_file, open(output_file_path, 'r') as output_file:
                status = subprocess.run([sys.executable,file_path], input=input_file.read(), capture_output=True, text=True, timeout=time_limit)
                if status.returncode != 0:
                    # print(f"RTE on test case {index}")
                    return "RTE", i
                else: 
                    if status.stdout.strip() != output_file.read().strip():
                        # print(f"WA on test case {index}")
                        return "WA", i

    except subprocess.TimeoutExpired:
        # print(f"TLE on test case {index}")
        return "TLE", i
    
    return "AC", i
    
def complie(file_path, test_name, time_limit): 
    if complie_error(file_path):
        return "CE", 0
    else: 
        test_folder = os.path.join(currpath, "test_folder", f"{test_name}")
        result, test_passed = detect_RTE_TLE_AC(file_path,test_folder,test_name,time_limit)
        return result, test_passed