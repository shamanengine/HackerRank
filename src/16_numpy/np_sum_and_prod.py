'''
You are given a 2-D array with dimensions NxM.
Your task is to perform the  tool over axis 0 and then find the product of that result.
Input Format
The first line of input contains space separated values of N and M.
The next N lines contains M space separated integers.
Output Format
Compute the sum along axis 0. Then, print the product of that sum.
'''
import numpy

n, m = map(int, input().split(" "))
a = numpy.array([list(map(int, input().split())) for _ in range(n)], int)

# print(a)
print(numpy.product(numpy.sum(a, axis=0)))
'''
Sample Input
2 2
1 2
3 4
Sample Output
24
'''
