import os
import folder_checking as fc
import clang as cl 
import pythonlang as pl

currfolder = os.getcwd()
paths = [
    "test_folder",
    "pending/C++", 
    "pending/Python",
    "processed/AC",
    "processed/WA",
    "processed/CE",
    "processed/RTE",
    "processed/TLE"
    ]

for i in paths: 
    if not fc.check_folder_2(currfolder, i):
        exit(0)

number_of_test = len(os.listdir(paths[0]))
number_of_code_1 = len(os.listdir(paths[1]))
number_of_code_2 = len(os.listdir(paths[2]))

if number_of_code_1!=0: 
    for i in os.walk(paths[1]): 
        for filename in i[2]: 
            if filename.endswith(".cpp"): 
                exit()
                # cl.complie(filename)

if number_of_code_2!=0: 
    for j in os.walk(paths[2]): 
        for filename in j[2]: 
            if filename.endswith(".py"): 
                exit()
                # pl.complie(filename)