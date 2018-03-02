# -*- coding: utf-8 -*-
#
# STUDENT ID = G00364787
# EXERCISE 04
# script to find Smallest multiple evenly divisable by numbes 1...20
# PROJECT EULER - PROBLEM 5
#
# see:  https://projecteuler.net/problem=5
# written on 24-feb-2018
# 
# all own work with references as below
#
# references used:
# https://docs.python.org/3/tutorial/controlflow.html#if-statements
# accessed: 24-feb-2018
#
# https://www.tutorialspoint.com/python/python_strings.htm
# accessed: 24-feb-2018
#
# http://www.tutorialspoint.com/python/python_basic_operators.htm
# accessed: 24-feb-2018
#
#
numberRange = 20
yesStr = ""
#
#

def check_divisable(num1):
#function to testif the supplied number is evenly divisable by all numbers 1...20
        result=0;
        evencount=0;
        testnum=numberRange
        ok=1
        # this will scan down from 20....1  satisfying the specification
        while testnum > 0 and ok==1:
            # test that the result calculation is even   e.g. 120 / 20 = 6 (even)
            result = ( num1 / testnum) % 2
            if ( result == 0):
                evencount=evencount+1               
            else:
                ok=0
            testnum = testnum - 1            
                
#            result = num % testnum
#            testnum = testnum - 1            
#            if result  == 0:
#                evencount=evencount+1
#            else:
#                ok=0

        return(evencount)
    

# match routine to check for smallest number evenly divisable by 1...20
num = 0
yesno = 0
outputStr = ""
smallestnumber = 0
# function to find the smallest number divisable 1...20
print("Program is running...")
while smallestnumber < 1:
    # increase the step value by twice the value of the largest factor
    num = num + 1
    yesno = 0
    yesno = check_divisable(num)    
#    if yesno > 1:
    if yesno > 9:
        print("Checking: ",num," and the result is:",yesno)        
        
    if yesno == numberRange:
            smallestnumber = num
#
## output the discovered first number to be found evenly divisable by 1...20
## of announce that there isnt one
print("# The result of calculations:")
if smallestnumber > 0:
    outputStr = "# The smallest number evenly divisable by 1..."
    outputStr = outputStr + str(numberRange)
    outputStr = outputStr + " is "
    outputStr = outputStr + str(smallestnumber)
    print(outputStr)
else:
    print("# I can't find a number to suit.")
#       
#
#
# OUTPUT FROM PROGRAM    
#
#
#Program is running...
#Checking:  465585120  and the result is: 20
# The result of calculations:
# The smallest number evenly divisable by 1...20 is 465585120
