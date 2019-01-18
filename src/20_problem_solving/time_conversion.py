#!/bin/python3

import os
import sys


#
# Complete the timeConversion function below.
#
def timeConversion(s):
    # Write your code here.
    h, m, s = s.split(":")
    am_pm = s[2:]
    s = s[:2]

    # print(h + ":" + m + ":" + s + " " + am_pm)

    if am_pm == "AM" and h == "12":
        h = "00"
    elif am_pm == "PM":
        if h != "12":
            h = str(int(h) + 12)

    # print(h + ":" + m + ":" + s)

    return (h + ":" + m + ":" + s)


if __name__ == '__main__':
    s = input()

    print(timeConversion(s))
    #
    #
    # f = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # s = input()
    #
    # result = timeConversion(s)
    #
    # f.write(result + '\n')
    #
    # f.close()
