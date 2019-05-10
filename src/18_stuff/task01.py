'''
Sum all 2-digit numbers from the sequence
'''

arr = list(map(int, input().strip().split()))
print(sum([x for x in arr if (10 <= x <= 99) or (-99 <= x <= -10)]))

'''
Input
1 2 3 11 322 20 9989 99
1 2 3 11 322 20 9989 -99

Output 
130
-68
'''
