'''
Write a script that takes three strings from the user and prints the one with the most characters.

'''
Sentence = input("Enter a phrase: ")
Sen2 = input("and a second one: ")
Sen3 = input("and one more: ")
mylist= [Sentence, Sen2, Sen3]
print(max(mylist, key=len))


