# AUTHOR = PAUL KEARNEY  
# STUDENT ID = G00364787
# DATE: 2018-01-23
#
# THIS IS AN AMALGAMATION OF WEEK01 AND WEEK02 SOURCE CODE 
# AND OUTPUT 
# AND COMMENTS MADE IN THE DICUSSIONGROUP
#
# EXERCISE 01
#
# filename= gmit--week01--FIBINACCI--20180123.py
#
# STUDENT ID= g00364787
# FINONACCI NUBMERS

# Ian McLoughlin
# A program that displays Fibonacci numbers.


def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

## define the variables
x = 0
y = 0
z = 0
l = 0
i = 0
nam = ""
opstr = ""
op = ""

## obtain user input
nam = input("Your name:")

## process user input
l = len(nam)
x = ord(str.upper(nam[0]))
y = ord(str.upper(nam[l-1]))

## convert ascii to position in alphabet
x = x-64
y = y-64

## display the two letters to operate on
print("The two letters to operate on are: ",nam[0], "(",x,") and ",nam[l-1],"(",y,")")

## add the two ''letters'' together
z = x+y

## calculate the result
ans = fib(z)

## display the result
## print("The Fibonacci number for your name: ", nam, " is: ", ans)
op = "My name is "
op = op + nam
op = op + ", so the first and last letter of my name ("
op = op + str.upper(nam[0])
op = op + " + "
op = op + str.upper(nam[l-1])
op = op + " = "
op = op + str(x)
op = op + " + "
op = op + str(y) + ") give the number " + str(z) + "."
op = op + "  The " + str(z) + "th Fibonacci number is " + str(ans) + "."
print(op)

## end
#
#
#
#
#
#
# WEEK 02
# G00364787
#
# Above is a link to a program I wrote that works similarly to last 
# week's exercise. Copy and run the program yourself. 
# Change the string variable to contain your own surname, and rerun it. 
# #Can you figure out what ord() does? 
# Try to Google it to find out. 
# Post the output of the program, along with any insight you have as 
# to what ord() does, to the discussions forum.
#
#
# Ian McLoughlin
# A program that displays Fibonacci numbers using people's names.

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

name = "KEARNEY"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)


#
#
#
