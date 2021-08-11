'''
Sample Input
8
UDDDUDUU
Sample Output
1
'''

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    elev = elev_b = count = 0
    for step in path:
        if step == 'U':
            elev = elev_b + 1
        elif step == 'D':
            elev = elev_b - 1

        if elev_b == 0 and elev < 0:
            count += 1
        elev_b = elev

    return count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    steps = int(input().strip())
    path = input()
    result = countingValleys(steps, path)
    print(result)
    # fptr.write(str(result) + '\n')
    # fptr.close()
