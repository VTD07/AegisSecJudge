# AegisSecJudge
> ### A judge for OJ platforms

---

> [!IMPORTANT]
>
> This project was created for learning purposes by a cyber security -  DevSecOps learner
>
> **Update (2026/02)**
> - Developing with docker with WSL2 on Windows 11. 

---

## Introduction 

**AegisSecJudge** is a judger which is developed best for perfomance and  security for linux servers. Aegis in ancient Greece stands for shields, symbols of DevSecOps . Fully developed by VTD12 - student from HUST. 

### Core Features

- Currently supporting for VietNamese education and market with three programming languages: C/C++/Python. 
- Real time feedback per test cases for each submissions. 
- View detailed evaluation results including test case feedback.
- Multiple verdict types: Accepted (AC), Wrong Answer (WA), Time Limit Exceeded (TLE), Memory Limit Exceeded (MLE), Runtime Error (RE), Compilation Error (CE).
- Execution time and memory usage tracking.
- Secure sandboxed code execution.

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

---

## Installation Steps

### 1. Clone the repository
```bash
git clone https://github.com/VTD07/AegisSecJudge
```

### 2. Run the application
```bash
python main.py
```

## Project Structure

```
AegisSecJudge/
│
├── main.py                             #synthesis of Judger
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
│   └── test_comparison.py              #Test comparison logic for each type
│
├── pre_check/                          #Check for prerequisites
│   ├── __init__.py
│   ├── check_condition.py              #Check for folder, compiler
│   └── folder_checking.py              #Check for folder and permissions
│
├── pending/                            #Template file for judge
│   └── cpp/
│
├── db/                                 #Database (currently developing)
│
└── test_folder/                        #Test of each problems
    └── <problem_id>/
        └── Test01/
            ├── <id>.inp
            └── <id>.out
```

---
