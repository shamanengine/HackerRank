#!/bin/python3
import math
import os
import random
import re
import sys


def repeatedString(s, n):
    # Write your code here
    count = count_t = 0
    for l in s:
        if l == 'a':
            count += 1

    for l in s[:n % len(s)]:
        if l == 'a':
            count_t +=1

    # res = (n // len(s)) * count + s[:n % len(s)]
    res = (n // len(s)) * count + count_t
    return res


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    n = int(input().strip())
    result = repeatedString(s, n)
    print(result)
    # fptr.write(str(result) + '\n')
    # fptr.close()
