from collections import OrderedDict


def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    m = int(n / k)

    for i in range(m):
        print("".join(OrderedDict.fromkeys(string[i * k:(i + 1) * k]).keys()))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

"""Input:
AABCAAADA
3

Output:
AB
CA
AD
"""
