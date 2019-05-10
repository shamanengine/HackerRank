def solution(N):
    arr = str(N)
    hashtable = [0] * 10
    res = ""

    for el in arr:
        hashtable[int(el)] += 1

    for ind in range(9, -1, -1):
        res += hashtable[ind] * str(ind)

    res = int(res)

    if res > 10 ** 8:
        res = -1

    return res
