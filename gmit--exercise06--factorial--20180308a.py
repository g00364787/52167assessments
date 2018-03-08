# -*- coding: utf-8 -*-
#
# AUTHOR = PAUL KEARNEY  
# STUDENT ID = G00364787
# DATE = 2018-03-08
# 
# all own work - no references used
#
#Exercise 6
#
#Please complete the following exercise this week. 
#Write a Python script containing a function called factorial() that takes 
#a single input/argument which is a positive integer and returns its factorial.
#The factorial of a number is that number multiplied by all of the positive 
#numbers less than it. For example, the factorial of 5 is 5x4x3x2x1 which 
#equals 120. You should, in your script, test the function by calling it with 
#the values 5, 7, and 10.

# setup variables before using them
number = 0
total = 0

# function to calculate the FACTORIAL value of a supplied positive number
def factorial(num1):
    total = 1
    num2 = 1
    if ( num1 > 0 ):
        while ( num2 <= num1):
            total = total * num2
            num2 = num2 + 1
    return total

# function to announce the values to screen
def showToScreen(num,tot):
    opStr = ""
    opStr = "Called FACTORIAL with number:" + str(num).rjust(3," ")+"."
    opStr = opStr + " The returned value: " + str(tot).rjust(8," ")
    print (opStr)
    

# code to test FACTORIAL function
number = 5
total = factorial(number)
showToScreen(number,total)

number = 7
total = factorial(number)
showToScreen(number,total)

number = 10
total = factorial(number)
showToScreen(number,total)



# sample output from the above code
#Called FACTORIAL with number:  5. The returned value:      120
#Called FACTORIAL with number:  7. The returned value:     5040
#Called FACTORIAL with number: 10. The returned value:  3628800



