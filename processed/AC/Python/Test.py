def merge_dict(d1, d2):
    dict={}
    for key in d1: 
        dict[key]=d1[key]+d2.get(key,0)
    for key in d2: 
        if not key in dict: 
            dict[key]=d2[key]
    return dict
        
    
print(merge_dict({'a': 3, 'b': 2, 'c': 1}, {'b': 3, 'c': 2, 'd': 1}))