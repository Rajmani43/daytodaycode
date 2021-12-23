#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    total_sum = 0
    min = max = arr[0]
    for i in range(len(arr)):
        total_sum += arr[i]
    for i in range(len(arr)):
        if min > arr[i]:
            min = arr[i]
        if max < arr[i]:
            max = arr[i]
    print(total_sum - max , total_sum -min)
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
