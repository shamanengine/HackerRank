'''
You are given the shape of the array in the form of space-separated integers,
each integer representing the size of different dimensions,
your task is to print an array of the given shape and integer type using the tools numpy.zeros and numpy.ones.'''

import numpy

# n, m, p = map(int, input().split())
*args, = map(int, input().split())

zeros = numpy.zeros(args, dtype=numpy.int)
ones = numpy.ones(args, dtype=numpy.int)

print(zeros, ones, sep='\n')

'''
print("Zeros", zeros)
print("Ones", ones)
arr1 = numpy.array([zeros for _ in range(p)])
arr2 = numpy.array([ones for _ in range(p)])
print("=Answer=")
'''

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
'''
Input
3 2
Expected Output
[[0 0]
 [0 0]
 [0 0]]
[[1 1]
 [1 1]
 [1 1]]
'''

'''
Input
3 2 2 2

Output
[[[[0 0]
   [0 0]]

  [[0 0]
   [0 0]]]


 [[[0 0]
   [0 0]]

  [[0 0]
   [0 0]]]


 [[[0 0]
   [0 0]]

  [[0 0]
   [0 0]]]]
[[[[1 1]
   [1 1]]

  [[1 1]
   [1 1]]]


 [[[1 1]
   [1 1]]

  [[1 1]
   [1 1]]]


 [[[1 1]
   [1 1]]

  [[1 1]
   [1 1]]]]
'''