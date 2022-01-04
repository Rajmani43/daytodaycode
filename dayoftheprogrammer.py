#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Write your code here
    #leap year has 366 days
    leap_year = 0
    if year == 1918:
        return "26.09.%s" % year
    if year <  1918:
        #Julian Calendar 
        if (year % 4 == 0):
            leap_year = 1
        if leap_year == 1:
            time = "12.09.%s" % year
        else:  
            time = "13.09.%s" % year
        return time
    else:
        #Gregorian calendar
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            leap_year = 1   
        if leap_year == 1:
            time = "12.09.%s" % year
        else:  
            time = "13.09.%s" % year
        return time
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result+ '\n')

    fptr.close()
