n = int(input())
s = set(map(int, input().strip().split()))
N = int(input())

for _ in range(N):
    command, *arguments = input().strip().lower().split()
    # print(command)
    if "pop" == command:
        s.pop()
    elif "remove" == command:
        s.remove(list(map(int, arguments))[0])
    elif "discard" == command:
        s.discard(list(map(int, arguments))[0])

print(sum(s))
