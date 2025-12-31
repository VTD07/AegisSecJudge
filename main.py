import os
import sqlite3 as sql
from data.tests import build_test_cases
from data.load_problem_condition import setup_condition
from judge.judge import process_sumbission

currpath = os.getcwd()
db="db\\SQLite.db"
path_db = os.path.join(currpath, db)
conn = sql.connect(path_db)
    
cursor = conn.cursor()

cursor.execute('''SELECT id, time_limit, memory_limit from problem''')
problem_condition = cursor.fetchall()
condition = setup_condition(problem_condition)

cursor.execute('''SELECT input_data,output_data,problem_id FROM test_case ''')
test_cases = cursor.fetchall()
build_test_cases(currpath,test_cases)

cursor.execute('''SELECT id,problem_id, user_id, language, code FROM submission''')
submissions = cursor.fetchall()
process_sumbission(submissions,currpath,condition)

        
conn.close()