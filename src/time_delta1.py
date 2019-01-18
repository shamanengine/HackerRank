# Day dd Mon yyyy hh:mm:ss +xxxx
# Sun 10 May 2015 13:54:36 -0700

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the time_delta function below.
def time_delta(t1, t2):
    from datetime import datetime

    FMT = "%a %d %b %Y %H:%M:%S %z"
    t1 = datetime.strptime(t1, FMT)
    t2 = datetime.strptime(t2, FMT)

    return str(abs(int((t1 - t2).total_seconds())))


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())

    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        print(delta)

        # fptr.write(delta + '\n')

    # fptr.close()
