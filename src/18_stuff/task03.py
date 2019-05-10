def solution_naive(N):
    arr = reversed(sorted(list(str(N))))
    res = int("".join(map(str, arr)))

    if res > 10 ** 8:
        res = -1

    return res


if __name__ == '__main__':
    print(solution_naive("2642"))
