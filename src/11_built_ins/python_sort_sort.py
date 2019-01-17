#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    for attr in sorted(arr, key=lambda x: x[k]):
        print(" ".join(map(str, attr)))

'''
Sample Input 0
5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1

Sample Output 0
7 1 0
10 2 5
6 5 9
9 9 9
1 23 12
'''
