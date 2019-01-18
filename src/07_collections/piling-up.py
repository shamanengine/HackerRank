for _ in range(int(input())):
    n = int(input())
    horizontal = list(map(int, input().strip().split()))

    if n > 100:
        hor = list()
        hor.append(horizontal[0])
        for i in range(1, n - 2):
            if horizontal[i] != horizontal[i + 1]:
                hor.append(horizontal[i])
        n = len(hor)
    else:
        hor = horizontal

    s = "Yes"
    for i in range(n - 1):
        if hor[0] == max(hor):
            hor = hor[1:]
        elif hor[-1] == max(hor):
            hor = hor[:-1]
        else:
            s = "No"
            break

    print(s)
'''
Sample Input
2
6
4 3 2 1 3 4
3
1 3 2

Sample Output
Yes
No
'''
