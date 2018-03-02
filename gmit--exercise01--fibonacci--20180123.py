# AUTHOR = PAUL KEARNEY  
# DATE = 2018-01-23
# STUDENT ID = G00364787
# EXERCISE 01
#
# filename= gmit--exercise01--FIBINACCI--20180123.py
#
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
