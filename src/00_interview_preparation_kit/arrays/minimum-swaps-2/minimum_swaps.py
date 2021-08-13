#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    m = 0
    for i in range(len(arr) - 1):
        min_el = min(arr[i + 1:])
        if min_el < arr[i]:
            pos_min = arr.index(min_el)
            arr[i], arr[pos_min] = arr[pos_min], arr[i]
            m += 1
    return m


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = minimumSwaps(arr)
    print(res)
    # fptr.write(str(res) + '\n')
    # fptr.close()
