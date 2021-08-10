#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    available = set()
    m = 0
    for i in range(n):
        if ar[i] not in available:
            available.add(ar[i])
        else:
            available.remove(ar[i])
            m += 1
    return m


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    print(result)
    # fptr.write(str(result) + '\n')
    # fptr.close()

'''
Sample Input
STDIN
-----
9
10 20 20 10 10 30 50 10 20
Sample Output
3

10
1 1 3 1 2 1 3 3 3 3
4
'''