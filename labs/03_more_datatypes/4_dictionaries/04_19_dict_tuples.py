'''
Write a script that sorts a dictionary into a list of tuples based on values. For example:

input_dict = {"item1": 5, "item2": 6, "item3": 1}
result_list = [("item3", 1), ("item1", 5), ("item2", 6)]

'''
result_list = []
input_dict = {"item1": 5, "item2": 6, "item3": 1}
for k, v in input_dict.items():
    result_list.append((k, v))
output_list = sorted(result_list,key=lambda x: x[1])
print(output_list)