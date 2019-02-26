'''
Write a script that takes the following two dictionaries and creates a new dictionary by combining
the common keys and adding the values of duplicate keys together. For example:

_dict1 = {"a": 1, "b": 2, "c": 3}
_dict2 = {"a": 2, "c": 4 , "d": 2}

result = {"a": 3, "b": 2, "c": 7 , "d": 2}


'''
dic1 = {"a": 1, "b": 2, "c": 3}
dic2 = {"a": 2, "c": 4, "d": 2}

dic = {key:[] for key in list(dic1.keys()) + list(dic2.keys())}

for key in dic1.keys():
    dic[key].append(dic1[key])

for key in dic2.keys():
    dic[key].append(dic2[key])
print({k:sum(v) for k,v in dic.items()})



