'''
Take in 10 numbers from the user. Place the numbers in a list.
Calculate the product of all of the numbers in the list.
Also, find the largest number in the list.

Print the results.

'''

numbers = [int(n, 10) for n in input("gimme 10 numberz boi and u better separate them with spaces: ").split()]
list1 = list(numbers)
def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total

print(multiply(list1))
print(max(list1))



