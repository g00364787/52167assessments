# -*- coding: utf-8 -*-
#
# AUTHOR = PAUL KEARNEY  
# STUDENT ID = G00364787
# DATE = 2018-02-24
# week 5
# script to find largest palindrome product of two 3 digit numbers
# see:  https://projecteuler.net/problem=4
# written on 24-feb-2018
# 
# all own work
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


# function to test for a palindrome in the parameter 'result'
def check_pallindrome(yesno):
## function to test for a palindrome
    # counter fo matching charactes
    matchingChar = 0
    
    # reset the counter
    matchingChar = 0
    
    # set the teststring to operate on from the value supplied integer
    testStr = str(result)
    
    # setup two indexes to run left-right and right-left
    indx2 = len(str(result))-1
    for indx1 in range(len(testStr)):
        if testStr[indx1] == testStr[indx2] and indx2>=0:
            matchingChar = matchingChar +1
            indx2=indx2-1
            
    if ( matchingChar == len(testStr) ):
        yesno = 1
    else:
        yesno = 0
                  
    return(yesno)



# match routine to check for largest palindrome of 2x 3 digit numbers
num1 = 100
num2 = 100
result = 0
maxResult = 0

resultLength = 0
resultStr1 = ""
resultStr2 = ""

indx = 0
teststr = ""
matchingChar = 0
yesno = 0
yesno1 = 0
yesno2 = 0
outputStr = ""
# using range(1000) because this is  0....999
for num1 in range(1000):
    for num2 in range(1000):
        if num1 > 99 and num2 > 99:
            result = num1 * num2
            if result > 0 and result > maxResult:
                    yesno = check_pallindrome(result)
                    if yesno > 0:
                            print("# The number ",result,"is a palindrome.")
                            yesno1=num1
                            yesno2=num2
                            maxResult = result

## output the discovered max result(if any) and palindrome
## of announce that there isnt one
print("# The result of calculations:")
if maxResult > 0:
    OutputStr= "# The largest palindrome of two 3 digit numbers is: "
    OutputStr= OutputStr + str(yesno1) + " x " + str(yesno2) +" = "+ str(maxResult)
    print(OutputStr)
else:
    print("# I can't find a palindrome of two 3 digit numbers.")
       
