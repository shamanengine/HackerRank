'''
You are given a 1-D array, A. Your task is to print the floor, ceil and rint of all the elements of A.
Input Format
A single line of input containing the space separated elements of array A.

Output Format
On the first line, print the floor of A.
On the second line, print the ceil of A.
On the third line, print the rint of A.
'''
import numpy
# numpy.set_printoptions(sign=' ')
arr = numpy.array(list(map(float, input().split(" "))))
print(numpy.floor(arr), numpy.ceil(arr), numpy.rint(arr), sep="\n")

'''
Sample Input
1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9
Sample Output
[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
[  2.   3.   4.   5.   6.   7.   8.   9.  10.]
[  1.   2.   3.   4.   6.   7.   8.   9.  10.]
'''
