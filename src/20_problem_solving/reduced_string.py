# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the superReducedString function below.
def superReducedString(s):
    n = len(s)
    if n == 1:
        return (s)
    else:
        lst = list(s[0])
        for c in s[1:]:
            if len(lst) == 0 or lst[-1] != c:
                lst.append(c)
            else:
                lst.pop()

    return "Empty String" if len(lst) == 0 else "".join(lst)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    result = superReducedString(s)
    print(result)

    # fptr.write(result + '\n')
    # fptr.close()

'''
Sample Input 0
aaabccddd

Sample Output 0
abd

Sample Input 2
baab

Sample Output 2
Empty String
'''
