a = set(map(int, input().strip().split()))
n = int(input())
sets = []

for i in range(n):
    sets.append(set(map(int, input().strip().split())))

answer = True
for some_set in sets:
    if not len(a.difference(some_set)) == (len(a) - len(some_set)):
        answer = False
        break

print(answer)

'''
Sample Input 0
1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12

Sample Output 0
False
'''