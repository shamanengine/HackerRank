#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    # for i in range(len(apples)):
    #     apples[i] = apples[i] + a

    apples_pos = [_ + a for _ in apples]
    oranges_pos = [_ + b for _ in oranges]

    count_apples, count_oranges = 0, 0

    for apple_pos in apples_pos:
        if s <= apple_pos <= t:
            count_apples += 1

    for orange_pos in oranges_pos:
        if s <= orange_pos <= t:
            count_oranges += 1

    print(count_apples)
    print(count_oranges)


    # for i in range len(oranges):
    #     oranges[i] = oranges[i] + a


if __name__ == '__main__':
    st = input().split()
    s = int(st[0])
    t = int(st[1])

    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])

    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
'''
7 11
5 15
3 2
-2 2 1
5 -6
'''
