'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''
i = int(input("investment amount"))
r = int(input("interest rate in percentage"))
y = int(input("number of years to invest"))
value = i*((1+r)/100)**y
print(value)
