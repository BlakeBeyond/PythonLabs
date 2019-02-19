'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''
x = str(input("gimme a sentence innit: "))
z = x.split()
def most_common(z):
    return max(set(z), key=z.count)
print(most_common(z))