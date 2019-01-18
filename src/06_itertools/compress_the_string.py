# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import groupby

s = input()
lst = list()
for key, group in groupby(s, lambda x: x[0]):
    res = "({}, {})".format(len(list(group)), key)
    lst.append(res)

print(" ".join(lst))

'''
Sample Input
1222311

Sample Output
(1, 1) (3, 2) (1, 3) (2, 1)
'''