'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''
#takes a number from the user
number = int(input("give me a number between 1 and 1,000,000,000: "))
if number %3 == 0:
    print("yup")
else:
    print("nope")


