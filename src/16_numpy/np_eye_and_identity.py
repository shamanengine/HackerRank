'''
Print an array of size NxM with its main diagonal elements as 's and 's everywhere else.

Input Format
A single line containing the space separated values of N and M.
N denotes the rows.
M denotes the columns.

Output Format
Print the desired X array.
'''
import numpy
# np.set_printoptions(legacy='1.13')
numpy.set_printoptions(sign=' ')
n, m = map(int, input().split(" "))
print(numpy.eye(n, m))

'''
Sample Input
3 3
Sample Output
[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]
'''