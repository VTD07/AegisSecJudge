import sqlite3 as sql
from complier import pythonlang,cpplang as pl,cppl
import os

db="db\\SQLite.db"
currpath = os.getcwd()
path_db = os.path.join(currpath, db)
conn = sql.connect(path_db)
condition = [0 for _ in range(1,1000000)]
test_counter = [0 for _ in range(1,1000000)]

cursor = conn.cursor()

cursor.execute('''SELECT id, time_limit, memory_limit from problem''')
problem_condition = cursor.fetchall()

for row in problem_condition:
    id = row[0]
    time_limit = row[1]//1000
    memory_limit = row[2]
    condition[id]=time_limit

cursor.execute('''SELECT input_data,output_data,problem_id FROM test_case ''')
test_cases = cursor.fetchall()

for test in test_cases: 

    inp = test[0]
    out = test[1]
    problem_id = test[2]
    
    test_folder = os.path.join(currpath, "test_folder", f"{problem_id}")
    if not os.path.exists(test_folder): os.mkdir(test_folder)
    test_counter[problem_id]+=1
    sub_test_folder = os.path.join(test_folder, f"Test{test_counter[problem_id]:02d}")
    os.makedirs(sub_test_folder,exist_ok=True)
    inp_path = os.path.join(sub_test_folder, f"{problem_id}.inp")
    out_path = os.path.join(sub_test_folder, f"{problem_id}.out")
    with open(inp_path,"w",encoding="utf-8") as intest, open(out_path,"w",encoding="utf-8") as outtest: 
        intest.write(inp)
        outtest.write(out)

cursor.execute('''SELECT id,problem_id, user_id, language, code FROM submission''')
submissions = cursor.fetchall()

for row in submissions:
    
    id = row[0]
    problem_id = row[1]
    user_id = row[2]
    language = row[3]
    code = row[4]
        
    if language == "cpp": 
        file_path = os.path.join(currpath, f"pending\\cpp\\{id}_{problem_id}_{user_id}.cpp")
        with open(file_path, 'w', encoding="utf-8") as file:
            file.write(code)
        
        status, total_test, test_passed, detailed = cppl.compile_cpp(file_path,problem_id,condition[problem_id])
        
        print(f"id: {id} | user_id: {user_id} | problem_id: {problem_id} | Status: {status} | Total_test: {total_test} | Test_passed: {test_passed}")
        for i in detailed: 
            print(i)
        
        print("-----------------------------------------------------------------")
    elif language == "python": 
        file_path = os.path.join(currpath, f"pending\\cpp\\{id}_{problem_id}_{user_id}.cpp")
        with open(file_path, 'w', encoding="utf-8") as file:
            file.write(code)
        
        status, test_passed = pl.complie(file_path,problem_id,condition[problem_id])
        print(f"user_id: {user_id} | problem_id: {problem_id} | Status: {status} | Test_passed: {test_passed}")

        
conn.close()