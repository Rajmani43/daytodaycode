#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    out_arr = []
    a_sum = 0
    b_sum = 0 
    for i in range(len(a)):
        if a[i] > b[i]:
            a_sum = a_sum + 1
    out_arr.append(a_sum)
    for i in range(len(b)):
        if b[i] > a[i]:
            b_sum = b_sum +1
    out_arr.append(b_sum)
    return out_arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
