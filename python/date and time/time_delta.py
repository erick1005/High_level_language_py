#!/bin/python3

'''reads the number of test cases, then for each test case, it reads two dates as strings, calculates the absolute difference between these two dates in seconds using the time_delta function, and writes this difference to a file.'''

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    
    #date format is Day dd Mon yyyy hh:mm:ss +xxxx
    d_format = "%a %d %b %Y %H:%M:%S %z"
    date1 = datetime. strptime(t1, d_format)
    date2 = datetime. strptime(t2, d_format)
    
    diff = int(abs(date1 - date2))

    #convert float difference into int
    return int(diff.total_seconds())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)


        #remember to cast it into a string before writing the results
        fptr.write(str(delta) + '\n')

    fptr.close()
