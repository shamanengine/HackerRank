def generalizedGCD(num, arr):
    # WRITE YOUR CODE HERE
    if num < 2:
        return arr

    tmp_gcd = arr[0]
    for i in range(num - 1):
        tmp_gcd = gcd(tmp_gcd, arr[i + 1])

    return tmp_gcd


def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


n1 = 5
arr1 = [2, 3, 4, 5, 6]

n2 = 5
arr2 = [2, 4, 6, 8, 10]

print(generalizedGCD(n1, arr1))
print(generalizedGCD(n2, arr2))

[2, 4, 6, 8, 10]

'''
Input 1
5,
[2, 3, 4, 5, 6]

Output 1
1

Input 2
5,
[2, 4, 6, 8, 10]
2
'''
