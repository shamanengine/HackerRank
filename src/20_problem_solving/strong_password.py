#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumNumber function below.
def minimumNumber(n, password):
    """Return the minimum number of characters to make the password strong
    Its length is at least 6.
    It contains at least one digit.
    It contains at least one lowercase English character.
    It contains at least one uppercase English character.
    It contains at least one special character. The special characters are: !@#$%^&*()-+
    She typed a random string of length  in the password field but wasn't sure if it was strong. Given the string she typed, can you find the minimum number of characters she must add to make her password strong? Note: Here's the set of types of characters in a form you can paste in your solution:
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    count = 0
    cases = [r'[a-z]', r'[A-Z]', r'[\d]', r'[!@#$%^&*()\-+]']
    for case in cases:
        if not re.search(case, password):
            count += 1

    return max(count, 6 - n)

    """
    i = 0
    if not re.search(r'[0-9]+', password):
        i += 1
    if not re.search(r'[a-z]+', password):
        i += 1
    if not re.search(r'[A-Z]+', password):
        i += 1
    if not re.search(r'[!@#$%^&*()\-+]+', password):
        i += 1

    return max(i, 6 - len(password))

    # return True if re.search(r'^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()\-+])(?=.{6,})', password) else False


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    password = input()
    answer = minimumNumber(n, password)

    print(answer)

    # fptr.write(str(answer) + '\n')
    # fptr.close()

'''
Sample Input -1
7
aB1$zxc

Sample Input 0
3
Ab1
Sample Output 0
3

Sample Input 1
11
#HackerRank
Sample Output 1
1
'''
