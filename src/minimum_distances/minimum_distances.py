#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumDistances function below.
def minimumDistances(a):
    i = 1
    distance = -1

    for element in a:
        b = a[i:]
        if element in b:
            new_distance = b.index(element) + 1
            if distance == -1 or new_distance < distance:
                distance = new_distance
        i += 1

    return distance


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().strip().split()))
    result = minimumDistances(a)
    print(result)

# fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
# n = int(input())
#
# a = list(map(int, input().rstrip().split()))
#
# result = minimumDistances(a)
#
# fptr.write(str(result) + '\n')
#
# fptr.close()
