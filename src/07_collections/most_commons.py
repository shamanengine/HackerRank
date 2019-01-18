#!/bin/python3

from collections import OrderedDict

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    s = input()

ordered_dict = OrderedDict()

for c in s:
    if c in ordered_dict:
        ordered_dict[c] += 1
    else:
        ordered_dict[c] = 1

ordered_dict = OrderedDict(sorted(ordered_dict.items(), key=lambda x: x[0], reverse=False))
ordered_dict = OrderedDict(sorted(ordered_dict.items(), key=lambda x: x[1], reverse=True))

i = 0
for key, value in ordered_dict.items():
    print("{} {}".format(key, value))
    i += 1
    if i > 2:
        break
'''
Sample Input 0
aabbbccde

Sample Output 0
b 3
a 2
c 2
'''
