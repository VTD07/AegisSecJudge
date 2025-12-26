import subprocess
import os 

currpath = os.getcwd()

def compile_cpp(file_path):
    exe_path = os.path.splitext(file_path)[0] + ".exe"
    status = subprocess.run(["g++", file_path,"-o", exe_path],capture_output=True,text=True)

    if status.returncode != 0:
        return None
    return exe_path

def detect_RTE_TLE_AC(file_path,test_folder,test_id,time_limit):
    try:
        
        for i in range(1,len(os.listdir(test_folder))+1):
            
            index=f"{i:02d}"
            
            input_folder_path = os.path.join(test_folder,f"Test{index}")
            input_file_path=os.path.join(input_folder_path,f"{test_id}.inp")
            output_file_path=os.path.join(input_folder_path,f"{test_id}.out")

            with open(input_file_path, 'r') as input_file, open(output_file_path, 'r') as output_file:
                status = subprocess.run([file_path], input=input_file.read(), capture_output=True, text=True, timeout=time_limit)
                if status.returncode != 0:
                    return "RTE", i-1
                else: 
                    if status.stdout.strip() != output_file.read().strip():
                        # print(f"WA on test case {index}")
                        return "WA" ,i-1

    except subprocess.TimeoutExpired:
        # print(f"TLE on test case {index}")
        return "TLE", i-1
    
    return "AC", i
    
def complie(file_path,test_name,time_limit): 
    exe_path = compile_cpp(file_path)
    test_folder = os.path.join(currpath, "test_folder", f"{test_name}")
    if exe_path is None:
        return "CE", 0
    else:
        result, test_passed = detect_RTE_TLE_AC(exe_path,test_folder,test_name,time_limit)
        return result, test_passed