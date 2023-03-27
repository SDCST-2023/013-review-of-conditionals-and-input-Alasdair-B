"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""

import math
print("\n\nThis calculator is used to find a missing side length in a right triangle")
a = 0.0
b = 0.0
c = 0.0

def ina():
    global a
    a = float(input("Enter length of the first side, if unknown, type \"0\""))
    if a < 0:
        print("Side lengths can\'t be negative ya clown, try again:")
        ina()
    else:
        inb()

def inb():
    global b
    b = float(input("Enter length of the second side, if unknown, type \"0\""))
    if b < 0:
        print("This calculator will allow negative sides just as soon as you figure out how to measure a negative length, try again stupid:")
        inb()
    elif a == 0 and b == 0 and c == 0:
        print("\nWow you sure do have a really nice patch of empty space")
        Pythagoras()
    else:
        check()

def inc():
    global c
    global a
    global b
    c = float(input("Enter length of the hypoteneuse, if unknown, type \"0\""))
    if c < 0:
        print("Now just how the hell is a negative length supposed to be the longest side of a triangle? let's try that one again:")
        inc()
    else:
        ina()
            

def check():
        global a
        global b
        global c

        unknown = 0

        if a==0:
            unknown = unknown + 1

        if b==0:
            unknown = unknown + 1

        if c==0:
            unknown = unknown + 1   

        if unknown == 2:
            print("\nNot enough sides are known, this is a triangle calculator, you gave it a singular line, what did you expect was gonna happen?")
            Pythagoras()

        if unknown == 1:
            if a==0:
                a = ((c**2) - (b**2))**0.5
                print("\nYour missing side 'a' has a length of: " + str(a))
                Pythagoras()
            if b==0:
                b = ((c**2) - (a**2))**0.5
                print("\nYour missing side 'b' has a length of: " + str(b))
                Pythagoras()
            if c==0:
                c = ((a**2) + (b**2))**0.5
                print("\nYour missing side 'c' has a length of: " + str(c))
                Pythagoras()
    
        if a >= c or b >= c:
            print("\nHypoteneuse has to be the longest side, you might want to take eigth grade math again")
            Pythagoras()
            
        if unknown == 0:
            print("\nThis triangle is already solved, what the hell were you planning to calculate?")
            Pythagoras()


def Pythagoras():
    print("\n")
    inc()
    
Pythagoras()
