'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''

#z = list(x)
#h = tuple(z)
#print(h)
# step 1 get input from the user
x = input("my body's so amazing so you thought you'd say sum: ")
#split the string using space as argument
string_list = x.split()
#chop up every item from a list
letterlist = []
for word in string_list:
    letter = tuple(word)
    letterlist.append(letter)
print(letterlist)


