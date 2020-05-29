#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    r = len(arr)
    c = len(arr[0])
    max = None
    while(r >= 3 ):
        temp = c
        while(temp >= 3):
            if max is None:
                sum = sumfunction(arr, r, temp)
                max = sum
            else:
                sum = sumfunction(arr, r, temp)
                if max < sum:
                    max = sum

            temp = temp - 1

        r = r - 1

    return max
            
        
def sumfunction(arr, r, c):
    sum = arr[r - 3][c - 3] + arr[r - 3][c - 2] + arr[r - 3][c - 1] + arr[r - 2][c - 2] + arr[r - 1][c - 1] + arr[r - 1][c - 2] + arr[r - 1][c - 3]
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
