import sys
import sqlite3 as sql
import os
import data_extract as de
import stat
import folder_checking as fc
import clang as cl 
import pythonlang as pl

##############
sys.dont_write_bytecode = True
##############

currfolder = os.getcwd()

os.chmod(os.path.join(currfolder,"test_folder"), stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)

paths = [
    "test_folder",
    "pending\\cpp", 
    "pending\\Python",
    ]

for i in paths:
    if not fc.check_folder_2(currfolder, i):
        print(f"{i} folder is missing")
        exit(0)

number_of_test = len(os.listdir(paths[0]))
number_of_code_1 = len(os.listdir(paths[1]))
number_of_code_2 = len(os.listdir(paths[2]))

print("C++ Test Results:")
if number_of_code_1!=0: 
    for i in os.walk(paths[1]): 
        for filename in i[2]: 
            if filename.endswith(".cpp"):
                cl.complie(os.path.join(paths[1], filename))

print("Python Test Results:")
if number_of_code_2!=0: 
    for j in os.walk(paths[2]): 
        for filename in j[2]: 
            if filename.endswith(".py"): 
                pl.complie(os.path.join(paths[2], filename))