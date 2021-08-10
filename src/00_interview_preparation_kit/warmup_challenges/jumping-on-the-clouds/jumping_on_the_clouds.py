#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the 'jumpingOnClouds' function below.
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.

def jumpingOnClouds(c):
    # Write your code here
    m = i = 0
    while i < len(c) - 1:
        if i + 2 < len(c) and c[i + 2] == 0:
            i += 2
        else:
            i += 1
        m += 1
    return m


'''
Sample Input 0
7
0 0 1 0 0 1 0
Sample Output 0
4
Sample Input 1
6
0 0 0 0 1 0
Sample Output 1
3
'''

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c)
    print(result)

    # fptr.write(str(result) + '\n')
    # fptr.close()
