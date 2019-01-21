"""
You are given a string S.
Your task is to find the indices of the start and end of K string in S.

Input Format
The first line contains the string S. The second line contains the string K.

Output Format
Print the tuple in this format: (start _index, end _index). If no match is found, print (-1, -1).
"""
import re

s, k = input(), input()

i = 0

while re.search(k, s[i:]):
    m = re.search(k, s[i:])
    start = m.start() + i
    end = m.end() + i - 1
    print("(" + str(start) + ", " + str(end) + ")")
    i += m.start() + 1

if i == 0:
    print("(-1, -1)")

#
# for m in re.findall(k, s):
#     print(m)
# print("(" + str(m.start()) + ", " + str(m.end()) + ")")

'''
Sample Input
aaadaa
aa

Sample Output
(0, 1)  
(1, 2)
(4, 5)
'''
