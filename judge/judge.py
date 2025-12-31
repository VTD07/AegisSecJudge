import os
import complier.cpplang as cppl 
import complier.pythonlang as pl

def return_result(id,user_id,problem_id,status,detailed,language,total_test,test_passed): 
    print(f"id: {id} | user_id: {user_id} | problem_id: {problem_id} | Language: {language} | Status: {status} | Total_test: {total_test} | Test_passed: {test_passed}")
    for i in detailed: 
        print(i)
    
    print("-----------------------------------------------------------------")

def process(currpath,id,user_id,problem_id,code,language,extension,compiler,time_limit):
    file_path = os.path.join(currpath, f"pending\\cpp\\{id}_{problem_id}_{user_id}.{extension}")
    with open(file_path, 'w', encoding="utf-8") as file:
        file.write(code)
            
    status, total_test, test_passed, detailed = compiler(file_path,problem_id,time_limit)
    return_result(id,user_id,problem_id,status,detailed,language,total_test,test_passed)

    

def process_sumbission(submissions,currpath,condition):
    
    
    for row in submissions:
        
        id = row[0]
        problem_id = row[1]
        user_id = row[2]
        language = row[3]
        code = row[4]
        time_limit = condition[problem_id]
        
        if language == "cpp": 
            process(currpath,id,user_id,problem_id,code,language,"cpp",cppl.compile_cpp,time_limit)
        elif language == "python": 
            process(currpath,id,user_id,problem_id,code,language,"py",pl.compile_python,time_limit)