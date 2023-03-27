#!python3
"""
Debug this program so that it runs

program should read a float value
and use it as an exponent rounded to 2 decimal places

original code:
x = Input("enter a float number:")
round(x)
print(x)
"""

x = float(input("Enter a float number:\n"))
x = round(x, 2)
print(x)