'''
Write a script that creates a list of all unique values in a list. For example:

_list = [1, 2, 6, 55, 2,, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''
mylist = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
myset = set(mylist)
list1 = list(myset)
print(list1)