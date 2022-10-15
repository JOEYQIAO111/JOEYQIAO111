def get_max_score(score_dic):
    keys = list(dic.keys())
    values = list(dic.values())  

    max_n = max(values)  
    v_index = values.index(max_n)
    
    return keys[v_index]

dic = {
    '语文': 90,
    '数学': 97,
    '英语': 98
}

course = get_max_score(dic)

print(course)