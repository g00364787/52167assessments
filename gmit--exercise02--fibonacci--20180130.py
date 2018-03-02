# AUTHOR = PAUL KEARNEY  
# STUDENT ID = G00364787
# DATE = 2018-01-30
# STUDENT ID = G00364787
# EXERCISE 02
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