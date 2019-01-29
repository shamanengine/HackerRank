'''
You are given the shape of the array in the form of space-separated integers,
each integer representing the size of different dimensions,
your task is to print an array of the given shape and integer type using the tools numpy.zeros and numpy.ones.'''

import numpy

n, m, p = map(int, input().split())
zeros = numpy.zeros((n, m), dtype=numpy.int)
ones = numpy.ones((n, m), dtype=numpy.int)

arr1 = numpy.array([zeros for _ in range(p)])
arr2 = numpy.array([ones for _ in range(p)])
print(arr1, arr2, sep='\n')
'''
Input
3 2 3

Expected Output
[[[0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]]]
[[[1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]]]
'''
