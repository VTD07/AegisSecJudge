import sqlite3 as sql
import os

db="db\\SQLite.db"
currpath = os.getcwd()
path_db = os.path.join(currpath, db)
conn = sql.connect(path_db)

def extract_id(conn): 
    cursor = conn.cursor()
    cursor.execute('''SELECT id FROM submission''')
    ids = []
    for row in cursor.fetchall(): 
        ids.append(row[0])
    return ids

def code_extract(conn): 
    ids = extract_id(conn)
    cursor = conn.cursor()
    for id in ids:
        cursor.execute('''SELECT language, code FROM submission WHERE id=?''', (id,))
        for row in cursor.fetchall(): 
            language = row[0]
            code = row[1]
            print(language)
            if language == "cpp": 
                file_path = os.path.join(currpath, f"pending\\cpp\\{id}.cpp")
                with open(file_path, 'w', encoding="utf-8") as file:
                    file.write(code)
            elif language == "python":
                file_path = os.path.join(currpath, f"pending\\Python\\{id}.py")
                with open(file_path, 'w', encoding="utf-8") as file:
                    file.write(code)

code_extract(conn)

conn.close()