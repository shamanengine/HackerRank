from collections import deque

d = deque()
for _ in range(int(input())):
    command, *args = input().lower().split()
    if "append" == command:
        d.append(args[0])
    if "appendleft" == command:
        d.appendleft(args[0])
    elif "pop" == command:
        d.pop()
    elif "popleft" == command:
        d.popleft()

print(" ".join([_ for _ in d]))
