import subprocess
import os
import sys 

currpath = os.getcwd()

def detect_CE(file_path):
    status = subprocess.run([sys.executable, "-m", "py_compile", file_path], cwd=currpath, capture_output=True, text=True)
    return status.returncode != 0

def detect_RTE_TLE_AC(file_path,test_folder,test_id,time_limit):
    
    passed_test, total_test = 0, len(os.listdir(test_folder))
    RTE = TLE = MLE = WA = False 
    detailed = []
            
    for i in range(1,total_test+1):
        
        index=f"{i:02d}"
        
        input_folder_path = os.path.join(test_folder,f"Test{index}")
        input_file_path=os.path.join(input_folder_path,f"{test_id}.inp")
        output_file_path=os.path.join(input_folder_path,f"{test_id}.out")
        with open(input_file_path, 'r') as input_file, open(output_file_path, 'r') as output_file:
            try: 
                status = subprocess.run([sys.executable,file_path], input=input_file.read(), capture_output=True, text=True, timeout=time_limit)
                if status.returncode != 0:
                    detailed.append(("RTE",i))
                    RTE = True
                else: 
                    if status.stdout.strip() != output_file.read().strip():
                        # print(f"WA on test case {index}")
                        # return "WA" ,i-1
                        WA = True
                        detailed.append(("WA",i))
                    else: 
                        detailed.append(("AC",i))
                        passed_test+=1

            except subprocess.TimeoutExpired:
                # print(f"TLE on test case {index}")
                # return "TLE", i-1
                TLE = True
                detailed.append(("TLE",i))
    
    result=""
    
    if RTE == True: result = "RTE"
    elif TLE == True: result = "TLE"
    # elif MLE == True: result = "MLE"
    elif WA == True: result = "WA"
    else: result = "AC"
    
    return result, total_test, passed_test, detailed

    
def compile_python(file_path,test_name,time_limit): 
    exe_path = detect_CE(file_path)
    test_folder = os.path.join(currpath, "test_folder", f"{test_name}")
    if exe_path is None:
        return "CE",len(os.listdir(test_folder)), 0, ("CE",0)
    else:
        return detect_RTE_TLE_AC(exe_path,test_folder,test_name,time_limit)

