"""
&& → and
|| → or
Both && and || should have a space " " on both sides.

Input Format
The first line contains the integer, N.
The next N lines each contain a line of the text.
"""

import re

for _ in range(int(input())):
    s = input()
    s = re.sub(r'(?<=\s)&&(?=\s)', "and", s)
    s = re.sub(r'(?<=\s)\|\|(?=\s)', "or", s)
    print(s)

'''
for _ in range(int(input())):
    print(re.sub(r'(?<= )(&&|\|\|)(?= )',
                 lambda x: 'and' if x.group() == '&&' else 'or',
                 input()))
                 
'''

"""
Input (stdin)
1
x&& &&& && && x || | ||\|| x
Expected Output
x&& &&& and and x or | ||\|| x
"""

"""
Sample Input
11
a = 1;
b = input();
if a + b > 0 && a - b < 0:
    start()
elif a*b > 10 || a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.

Sample Output
a = 1;
b = input();
if a + b > 0 and a - b < 0:
    start()
elif a*b > 10 or a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.

"""
