#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    time_domain = s[-2:]
    hour = s[:2]
    minute = s[3:5]
    seconds = s[6:8]
    if time_domain == "PM":
        if int(hour) != 12 :
            new_hour = int(hour)+12
            return str(new_hour)+":"+minute+":"+seconds
        else:
            return hour+":"+minute+":"+seconds
    elif time_domain == "AM":
        if int(hour) == 12:
            new_hour = "00"
            return new_hour+":"+minute+":"+seconds
        else:
            return hour+":"+minute+":"+seconds
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
