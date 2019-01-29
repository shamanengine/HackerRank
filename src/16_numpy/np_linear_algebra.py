'''
You are given a square matrix A with dimensions NxN. Your task is to find the determinant.
Input Format
The first line contains the integer N.
The next N lines contains the N space separated elements of array A.
Output Format
Print the determinant of A.
'''
import numpy

# numpy.set_printoptions(legacy='1.13')
n = int(input())
arr = numpy.array([list(map(float, input().split(" "))) for _ in range(n)])
# print("%.2f" % numpy.linalg.det(arr))
print(numpy.linalg.det(arr))

'''
Sample Input
2
1.1 1.1
1.1 1.1
Sample Output
0.0

Input
2
1.1 1.1
1.1 1.2

Output
0.11
'''
