# WEEK 03
#
# filename= gmit--week03--collatz--20180205d.py
#
# STUDENT ID= g00364787
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