'''
You are given a space separated list of numbers.
Your task is to print a reversed NumPy array with the element type float.
Input Format
A single line of input containing space separated numbers.
Output Format
Print the reverse NumPy array with type float.
'''


# import numpy


def arrays(arr):
    # complete this function
    # use numpy.array
    return numpy.array(list(reversed(arr)), float)


arr = input().strip().split(' ')
# arr = "1 2 3 4 -8 -10".strip().split(' ')
result = arrays(arr)
print(result)
'''
Sample Input
1 2 3 4 -8 -10
Sample Output
[-10.  -8.   4.   3.   2.   1.]
'''
