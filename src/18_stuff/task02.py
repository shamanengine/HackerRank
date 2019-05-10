'''
Given 2 numbers, provide number of all perfect squares between them
'''
import math

a, b = map(int, input().strip().split())
i = 0
for x in range(int(math.ceil(a ** (1 / 2))), b):
    if x ** 2 <= b:
        i += 1
        # print(x)
    else:
        break

print(i)

'''
Input
1 50 
25590 26590
9 49

Output
7
4
5
'''
