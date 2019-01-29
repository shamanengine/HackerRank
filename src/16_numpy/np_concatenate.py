import numpy

N, M, P = map(int, input().strip().split(" "))

arr1 = numpy.array([input().split() for i in range(N)], int)
arr2 = numpy.array([input().split() for j in range(M)], int)

arr = numpy.concatenate((arr1, arr2), axis=0)
print(arr)
