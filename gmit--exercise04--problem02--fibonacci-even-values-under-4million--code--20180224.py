# AUTHOR = PAUL KEARNEY  
# STUDENT ID = G00364787
# DATE = 2018-02-24
#
# STUDENT ID = G00364787
# EXERCISE 04

# projectEuler   problem 2
# references used
# http://www.tutorialspoint.com/python/python_basic_operators.htm
# https://www.tutorialspoint.com/python/python_strings.htm
# https://stackoverflow.com/questions/9120059/odd-even-string-python
#

# function to calculate the FIBONACCI value for input value n
def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

# setup working storage
num = 0
total = 0
result = 0
total = 0
ok = 1
opStr = ""

# main routine
while result < 4000000 and ok == 1:    
    result = fib(num)
    if (result < 4000000):
        if (result %2 == 0 ):
            total = total+result 
    else:
        ok = 0
    num = num + 1

# program output to screen             
opStr = "The sum of the even numbers 'under' 4 million is "+ str(total) 
print(opStr)
    
