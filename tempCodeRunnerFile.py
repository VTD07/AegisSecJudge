print("C++ Test Results:")
if number_of_code_1!=0: 
    for i in os.walk(paths[1]): 
        for filename in i[2]: 
            if filename.endswith(".cpp"):
                cl.complie(os.path.join(paths[1], filename))
