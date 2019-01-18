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
    import datetime, calendar

    def t_to_dt(t):
        Day, d, m, y, hh, mm, ss, x = t.replace(":", " ").split()
        m = list(calendar.month_abbr).index(m)
        tz = datetime.timezone(datetime.timedelta(hours=int(x[:3]), minutes=int(x[3:])))

        return datetime.datetime(int(y), m, int(d), int(hh), int(mm), int(ss), tzinfo=tz)

    delta_seconds = (t_to_dt(t1) - t_to_dt(t2)).total_seconds()

    return str(int(abs(delta_seconds)))


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

'''
Sample Input 0
2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000

Sample Output 0
25200
88200
'''