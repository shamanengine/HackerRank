"""
Input Format
The first line contains the integer, , the length of the unencrypted string.
The second line contains the unencrypted string, .
The third line contains , the number of letters to rotate the alphabet by.

Output Format
For each test case, print the encoded string.
"""

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the caesarCipher function below.
def caesarCipher(s, k):
    lst = list()
    for c in s:
        if re.search(r'[A-Z]', c):
            number = ord(c) + k % (ord('Z') - ord('A') + 1)
            letter = chr(number) if number // (ord("Z") + 1) == 0 else chr(ord("A") + number % (ord("Z") + 1))
            lst.append(letter)
        elif re.search(r'[a-z]', c):
            number = ord(c) + k % (ord('z') - ord('a') + 1)
            letter = chr(number) if number // (ord("z") + 1) == 0 else chr(ord("a") + number % (ord("z") + 1))
            lst.append(letter)
        else:
            lst.append(c)

    # A - 65
    # Z - 90
    # a - 97
    # z - 122

    """
    _, s, k = input(), input(), int(input())

    def cipher(c):
        num = ord(c)
        if 97 <= num <= 122:
            return chr(((num - 97 + k) % 26) + 97)
        elif 65 <= num <= 90:
            return chr(((num - 65 + k) % 26) + 65)
        else:
            return c

    print(*[cipher(c) for c in s], sep='')
    """

    return "".join(lst)
"""
Sample Input
11
middle-Outz
2

Sample Output
okffng-Qwvb

Input (stdin)
10
www.abc.xy
87

Expected Output
fff.jkl.gh
"""

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    s = input()
    k = int(input())

    result = caesarCipher(s, k)
    print(result)

    # fptr.write(result + '\n')
    # fptr.close()
