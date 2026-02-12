# AegisSecJudge
> ### A judge for OJ platforms, working with 56-TECH

---

> [!IMPORTANT]
>
> This project was created for learning purposes by a Cyber Security -  DevSecOps learner.
>
> **Update (02/2026)**
> - Developing and testing with docker on WSL2 enviroment on Windows 11. 
> - Working with Memory Limit Exceeded (MLE) verdict.
---

## Introduction 

**AegisSecJudge** is a judger which is developed best for perfomance and security for linux servers. Aegis in ancient Greece stands for shields, symbols of security. Fully developed by VTD12 - student from HUST. 

### Core Features

- Currently supporting for VietNamese education market with three programming languages: C/C++/Python. 
- Real time feedback per test cases for each submissions. 
- View detailed evaluation results including test case feedback.
- Multiple verdict types: Accepted (AC), Wrong Answer (WA), Time Limit Exceeded (TLE), Memory Limit Exceeded (MLE), Runtime Error (RE), Compilation Error (CE).
- Execution time and memory usage tracking.
- Secure sandboxed code execution. (currently developing and testing with docker)

---

# Setup 

## Prerequisites 
* **Python and gcc and g++ complier installed**
* **pip** (Python package manager)
* **SQL**
* **Folder contain have reading and writing access**
* **Basic knowledge of Python and how complier work**

---

> [!CAUTION]
> Before running the Judge, ensure you have:
> - Installed all required dependencies 
> - Created necessary directories if deploying to production
> - You can run **check_condition.py** to check both of it.
---

## Installation Steps

### 1. Clone the repository
```bash
git clone https://github.com/VTD07/AegisSecJudge
```
### 2. Run check prerequisites program (Optional)
```bash
cd pre_check
python check_condition.py
```

### 2. Run the application
```bash
python main.py
```

## Project Structure

```
AegisSecJudge/
│
├── main.py                             #Synthesis of Judger
│
├── complier/                           #Test cases feedback and verdicts
│   ├── __init__.py                     
│   ├── cpplang.py                      #For C++ 
│   └── pythonlang.py                   #For Python
│
├── data/                               #Setup data for problems
│   ├── __init__.py
│   ├── load_problem_condition.py       #Load and setup problems conditions
│   └── tests.py                        #Load and setup test cases
│
├── judge/                              #Main judger
│   ├── __init__.py
│   ├── judge.py                        #Results of each submissions 
│   └── test_comparison.py              #Test comparison logic for each type of problem (currently developing)
│
├── pre_check/                          #Check for prerequisites
│   ├── __init__.py
│   ├── check_condition.py              #Check for folder, compiler and permissions.
│   └── folder_checking.py              #Check for folder and file exists
│
├── pending/                            #Temporary source file for judging
│   └── cpp/
│
├── db/                                 #Database -> Working for re-update feature working with back-end
│
└── test_folder/                        #Test of each problems
    └── <problem_id>/
        └── Test01/
            ├── <id>.inp
            └── <id>.out
```
