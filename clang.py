import subprocess
import os 

currpath = os.getcwd()
test_folder = os.path.join(currpath, "test_folder\\TONGCSNMOD")

def compile_cpp(file_path):
    exe_path = os.path.splitext(file_path)[0] + ".exe"
    status = subprocess.run(["g++", file_path,"-o", exe_path],capture_output=True,text=True)

    if status.returncode != 0:
        print(f"Compilation error in {file_path}")
        return None

    return exe_path

def detect_RTE_TLE_AC(file_path):
    try:
        
        for i in range(1,21):
            
            index=f"{i:02d}"
            
            input_folder_path = os.path.join(test_folder,f"Test{index}")
            input_file_path=os.path.join(input_folder_path,f"TONGCSNMOD.inp")
            output_file_path=os.path.join(input_folder_path,f"TONGCSNMOD.out")
            
            with open(input_file_path, 'r') as input_file, open(output_file_path, 'r') as output_file:
                status = subprocess.run([file_path], input=input_file.read(), capture_output=True, text=True, timeout=1)
                if status.returncode != 0:
                    # print(f"RTE on test case {index}")
                    return "RTE"
                else: 
                    if status.stdout.strip() != output_file.read().strip():
                        # print(f"WA on test case {index}")
                        return "WA"

    except subprocess.TimeoutExpired:
        # print(f"TLE on test case {index}")
        return "TLE"
    
    return "AC"
    
def complie(file_path): 
    exe_path = compile_cpp(file_path)
    if exe_path is None:
        print(f"Error: Compilation failed for {file_path}")
        exit(0)
    else:
        result = detect_RTE_TLE_AC(exe_path)
        print(f"Program resulted in: {result}")