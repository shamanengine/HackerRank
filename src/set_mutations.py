N = int(input().strip())
A = set(map(int, input().strip().split()))
M = int(input().strip())

for _ in range(M):
    command, length = input().strip().split()
    B = set(map(int, input().strip().split()))

    if command == "intersection_update":
        A.intersection_update(B)
    elif command == "update":
        A.update(B)
    elif command == "symmetric_difference_update":
        A.symmetric_difference_update(B)
    elif command == "difference_update":
        A.difference_update(B)

    # print(A)

print(sum(A))
