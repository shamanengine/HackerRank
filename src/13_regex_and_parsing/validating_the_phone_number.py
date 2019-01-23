# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(input())):
    print('YES' if re.match(r'[789][0-9]{9}$', input()) else 'NO')

'''
A valid mobile number is a ten digit number starting with 7, 8, 9.

Input Format
The first line contains an integer , the number of inputs.
lines follow, each containing some string.

Output Format
For every string listed, print "YES" if it is a valid mobile number and "NO" if it is not on separate lines. Do not print the quotes.

Sample Input
2
9587456281
1252478965

Sample Output
YES
NO
'''
