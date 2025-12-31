
condition = {}

def setup_condition(problem_condition):
    
    for row in problem_condition:
        id = row[0]
        time_limit = row[1]//1000
        memory_limit = row[2]
        condition[id]=time_limit
    
    return condition
