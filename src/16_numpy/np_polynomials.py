'''
You are given the coefficients of a polynomial P.
Your task is to find the value of P at point x.
Input Format
The first line contains the space separated value of the coefficients in P.
The second line contains the value of x.
Output Format
Print the desired value.
'''
import numpy

print(numpy.polyval(list(map(float, input().split(" "))), float(input())))
'''
Sample Input
1.1 2 3
0
Sample Output
3.0
'''