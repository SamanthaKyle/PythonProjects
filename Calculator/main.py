"""
Simple Calculator Project in Python
Author: Samantha Kyle
Date: May 14th, 2020

Simple calculator to re-familiarize myself with Python. Made alongside the course, "The Complete Python 3 Course:
Beginner to Advanced!" by Nick Jermain and Joseph Delgadillo on Udemy.

"""
# imports and initializing


import re

previous = 0
run = True

# function declarations


def perform_math():
    """This function performs math according to python eval() function,
    with guards in place so that user cannot tamper with code."""

    global run
    global previous

    equation = input(previous)
    if equation == 'X':
        run = False
    else:
        equation = re.sub('[^0-9+-/*%]', '', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            if re.sub('[+*/-]', '', equation) == equation:
                previous = equation
            else:
                previous = eval(str(previous) + equation)

# opening messages


print("Simple Calculator by Samantha Kyle")
print("Type X to escape.\n")

while run:
    perform_math()
