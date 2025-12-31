import os 

test_counter = {}

def build_test_cases(currpath,test_cases): 
    
    for test in test_cases: 

        inp = test[0]
        out = test[1]
        problem_id = test[2]
        
        if problem_id not in test_counter: test_counter[problem_id]=0

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
