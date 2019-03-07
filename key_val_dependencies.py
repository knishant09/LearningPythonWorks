



def key_depedencies():

    s_dict ={
    "A": ["B", "C", "D"],
    "B": ["E", "F"],
    "E" : ["G", "H"],
    "H" : ["I"],
    "J" : ["K"]


    }

   #{"A": "G", "I", "F", "C", "D"}
    #print(s_dict)

    lt = []
    for k,v  in s_dict.items():
        for elem in v:
            if elem not in s_dict.get(k):
                lt.append(elem)
            el









    print(dict_passval(s_dict, "A"))



def dict_passval(s_dict, k):


    list_1 = []
    if k not in s_dict:
        list_1.append(k)
    else:
        for v in s_dict.get(k):
            list_1.extend(dict_passval(s_dict, v))
    return list_1








key_depedencies()
