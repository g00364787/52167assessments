# AUTHOR = PAUL KEARNEY  
# DATE = 2018-02-05
# STUDENT ID = G00364787
# EXERCISE 02
#
# filename= gmit--exercise03--collatz--20180205d.py
#
#
# the  Collatz conjecture


print("The COLLATZ CONJECTURE")

# define the variables
num = ""
x = 0

# obtain user input
num = input("A start nummber: ")
x = int(num)

print("--Start of sequence.")
print (x)

# calculate the sequence/conjecture
while x != 1:
    if x % 2 == 0:
        x = x / 2
    else:
        x = (x * 3) + 1        

    print(int(x))
   
print("--End of sequence")   