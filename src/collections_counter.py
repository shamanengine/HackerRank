from collections import Counter

X = int(input())
sizes = Counter(list(map(int, input().split())))
N = int(input())
money = 0

for _ in range(N):
    args = list(map(int, input().split()))
    if sizes[args[0]] > 0:
        sizes[args[0]] -= 1
        money += args[1]

print(money)
