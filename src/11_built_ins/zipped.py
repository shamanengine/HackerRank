# A = [1, 2, 3]
# B = [6, 5, 4]
# C = [7, 8, 9]
# X = [A] + [B] + [C]
#
# print(X)
# print(*zip(X))
# print(*zip(*X))
#
# for _ in zip(*X):
#     print(_)
#     print(sum(_)/len(_))
#
# print(*zip(*X))
# X = zip(*X)
# print(*X)

N, X = map(int, input().split())
marks_list = []

for _ in range(X):
    marks_list += [list(map(float, input().split()))]

print("\n".join([str(sum(m)/ len(m)) for m in zip(*marks_list)]))

'''
Sample Input
5 3
89 90 78 93 80
90 91 85 88 86  
91 92 83 89 90.5

Sample Output
90.0 
91.0 
82.0 
90.0 
85.5    
'''