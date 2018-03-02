# -*- coding: utf-8 -*-
#
# AUTHOR = PAUL KEARNEY  
# STUDENT ID = G00364787
# DATE = 2018-03-02
# EXERCISE05
# A script to...
# Write a Python script that reads the Iris data set in and prints the four numerical 
# values on each row in a nice format. That is, on the screen should be printed the 
# petal length, petal width, sepal length and sepal width, and these values should 
# have the decimal places aligned, with a space between the columns.
# 
# all own work and with help from references
#
# references used:
# https://docs.python.org/2/library/csv.html
# accessed: 2-mar-2018
#
# https://pythonprogramming.net/reading-csv-files-python-3/
# accessed: 2 mar 2018
# 
# https://stackoverflow.com/questions/8234445/python-format-output-string-right-alignment
# accessed: 2 mar 2018
#
# http://www.tutorialspoint.com/python/string_rjust.htm
# accessed: 2 mar 2018
#
# http://www.tutorialspoint.com/python/string_rjust.htm
# accessed: 2 mar 2018
#
import csv
#
# setup the required data for the progam to run
filename = "iris.csv"
delim = ","
index = 0;

field = ""

print("# Program is running...")
with open(filename) as csvfile:
    print("# Opening: ",filename)
    readCSV = csv.reader(csvfile, delimiter=delim)
    for field in readCSV:
        if (len(field) >0 ):
            # build up the ouptut string before printing to screen.
            opStr =               field[0].rjust(3," ") + " " + field[1].rjust(3," ")
            opStr = opStr + " " + field[2].rjust(3," ") + " " + field[3].rjust(3," ")
            print( opStr )
    print("# End of file")
print("# Program is finished.")

