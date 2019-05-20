'''Sample Input 0
4
1 2 3 4

Sample Output 0
5

Sample Input 1
3
1 2 3

Sample Output 1
2
'''

n, arr = int(input()), list(map(int, input().split()))
max = arr[0] ^ arr[1]
for i in range(n - 1):
    for a in arr[i + 1:]:
        tmp = arr[i] ^ a
        print(str(arr[i]) + "^" + str(a) + "=" + str(tmp))
        if tmp > max:
            max = tmp

print(max)
