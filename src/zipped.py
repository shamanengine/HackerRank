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