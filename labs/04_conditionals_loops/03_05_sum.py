'''
Take two numbers from the user, an upper and lower bound. Using a loop, calculate the sum
	of numbers from the lower bound to the upper bound.

	For example, if a user enters 1 and 100, the output should be:
		The sum is: 5050
'''
r1 = int(input("give me a number: "))
r2 = int(input("another one: "))
x = sum(range(r1,r2+1))
print(x)

