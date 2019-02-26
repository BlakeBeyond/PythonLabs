'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''
number = int(input("enter a number between 0 and 1,000,000,000: "))
n = 0
while n >= 0:
    n = n+1
    if number == n:
        break
print(n)
