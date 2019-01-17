# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

if __name__ == '__main__':
    ordered_dict = OrderedDict()

    for _ in range(int(input())):
        s = input()
        if s in ordered_dict:
            ordered_dict[s] += 1
        else:
            ordered_dict[s] = 1

    print(len(ordered_dict))
    xx = list(ordered_dict.values())
    print(" ".join(map(str, xx)))

'''
4
bcdef
abcdefg
bcde
bcdef

3
2 1 1
'''
