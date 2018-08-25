# Symmetric Difference

if __name__ == '__main__':
    N, A = int(input()), set(map(int, input().split()))
    M, B = int(input()), set(map(int, input().split()))

    result = sorted(A.union(B).difference(A.intersection(B)))

    # doesn't work
    # print("\n".join(str(result)))
    print(*result, sep="\n")

    # works fine
    # for _ in result:
    #     print(_)
