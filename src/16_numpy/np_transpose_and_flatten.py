'''
You are given a NxM integer array matrix with space separated elements (N = rows and M = columns).
Your task is to print the transpose and flatten results.

Input Format
The first line contains the space separated values of N and M.
The next N lines contains the space separated elements of M columns.

Output Format
First, print the transpose array and then print the flatten.
'''

import numpy

N, M = map(int, input().split())
lst = list()
for i in range(N):  # rows
    # for j in M: # columns
    lst.append(list(map(int, input().split())))

arr = numpy.array(lst)

# print(arr)
print(numpy.transpose(arr))
print(arr.flatten())

# our_array = numpy.array([input().split() for y in range(int(input().split()[0]))], int)
# print(numpy.transpose(our_array), our_array.flatten(), sep="\n")

'''
Sample Input
2 2
1 2
3 4
Sample Output
[[1 3]
 [2 4]]
[1 2 3 4]
'''
