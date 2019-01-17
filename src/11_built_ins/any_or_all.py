N, args = int(input()), input().split()

print(args)
lst = [arg + '> 0' for arg in args]
print(lst)
print(all([eval(arg + ' > 0') for arg in args]))

print(all([eval(arg + ' > 0') for arg in args]) and any([arg == arg[::-1] for arg in args]))

'''
Sample Input
5
12 9 61 5 14

Sample Output
True
'''
